""" Asynchronous web server with aiohttp and kafka-aio"""

# main async web server
from aiohttp import web
import asyncio

# Messages exchanged with the stateful functions
from general_pb2 import ResponseMessage, RequestInfo

# Async kafka producer and consumer
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from aiokafka.errors import KafkaConnectionError, NoBrokersAvailable

# create the logger and configure
import logging
import uuid
import json
import time

from typing import Dict, Awaitable

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"

USER_EVENTS_TOPIC = "user-events"
ORDER_EVENTS_TOPIC = "order-events"
STOCK_EVENTS_TOPIC = "stock-events"
PAYMENT_EVENTS_TOPIC = "payment-events"

# timeout for waiting for a server response
TIMEOUT = 30

# Where yet to answer request messages
# are kept (request_id --> Future[json])
messages: Dict[str, Awaitable[str]] = {}

# The worker id that we'll use to identify
# messages addressed to us
WORKER_ID: str = str(uuid.uuid4())

# define the routes object
routes = web.RouteTableDef()


# Consume from the kafka topics forever
async def consume_forever(consumer: AIOKafkaConsumer):
    """ Infinite loop reading the messages
    sent from the flink cluster back to the application"""

    # Iterate through the messages and change the
    # future of the dict to be this result
    logger.info('Consumer starting to consumer messages')
    async for msg in consumer:
        # if the message is for our worker, get it
        if msg.key.decode('utf-8') == WORKER_ID:
            logger.info(f'Received message! {msg.value}')

            resp = ResponseMessage()
            resp.ParseFromString(msg.value)

            # set the result of the future in the dict
            if resp.request_id in messages:
                messages[resp.request_id].set_result(resp.result)
            else:
                logger.error('Received response for an unknown message')


async def create_kafka_consumer(app: web.Application):
    """ Starts the Kafka consumer and makes it accessible
    through the app object """
    logger.info('Starting kafka consumer...')

    broker_available = False

    while not broker_available:
        try:
            # Here we can set multiple topics to consume from
            # all at once and should work flawlessly
            consumer = AIOKafkaConsumer(
                USER_EVENTS_TOPIC,
                ORDER_EVENTS_TOPIC,
                STOCK_EVENTS_TOPIC,
                PAYMENT_EVENTS_TOPIC,
                loop=asyncio.get_running_loop(),
                bootstrap_servers=KAFKA_BROKER
            )
            await consumer.start()

            # Set the consumer accessible
            app['consumer'] = consumer

            # create the background task to run in parallel to
            # the main event loop
            asyncio.create_task(consume_forever(consumer))

            broker_available = True
            logger.info('Started consumer!')

        except (KafkaConnectionError, NoBrokersAvailable):
            await consumer.stop()
            time.sleep(4)
            continue


async def create_kafka_producer(app: web.Application):
    """ Creates the producer that the different endpoints
    will use to communicate with the statefuk functions """

    logger.info('Creating kafka producer...')

    broker_available = False

    while not broker_available:
        try:
            producer = AIOKafkaProducer(
                loop=asyncio.get_event_loop(),
                bootstrap_servers=KAFKA_BROKER
            )

            await producer.start()

            # set the producer accessible to all methods by means
            # of the app object
            app['producer'] = producer
            logger.info('Started producer!')

            broker_available = True

        except (KafkaConnectionError, NoBrokersAvailable):
            await producer.stop()
            time.sleep(4)
            continue


async def shutdown_kafka(app: web.Application):
    """ Gracefully stops the consumer and producer """
    logger.info('Stopping the consumer and producer')
    await app['consumer'].stop()
    await app['producer'].stop()


# Method to send a message and wait for a response
# from the server. Set the response for a given request
# to a future and then wait for completion of that future
async def send_msg(topic: str, key: str, request):
    """ Sends a message to a topic and wait for the
    future response which is then returned to the caller
    endpoint"""

    # set the request info
    request.request_info.worker_id = WORKER_ID
    request.request_info.request_id = str(uuid.uuid4())

    k = str(key).encode('utf-8')
    v = request.SerializeToString()

    # create a future and put it in the future messages dict
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    # add that future
    # the future will be set later by the kafka consumer
    messages[request.request_info.request_id] = fut

    await app['producer'].send_and_wait(topic, key=k, value=v)

    try:
        # Wait for the future
        result = await asyncio.wait_for(fut, timeout=TIMEOUT)

        # once we get the result (a json) delete the entry and return
        del messages[request.request_info.request_id]
        return result

    except asyncio.TimeoutError:
        logger.error('Timeout while waiting for message')

        # clean the entry and raise
        del messages[request.request_info.request_id]
        raise

# create the application object and add routes
app = web.Application()
app.add_routes(routes)

# get the routes from the particular endpoints
from orders_async_endpoint import routes_orders
from users_async_endpoint import routes_users
from payments_async_endpoint import routes_payments
from stock_async_endpoint import routes_stock

app.add_routes(routes_orders)
app.add_routes(routes_users)
app.add_routes(routes_payments)
app.add_routes(routes_stock)

# add the background tasks
app.on_startup.append(create_kafka_producer)
app.on_startup.append(create_kafka_consumer)

# add the shutdown tasks
app.on_cleanup.append(shutdown_kafka)

if __name__ == "__main__":
    web.run_app(app)
