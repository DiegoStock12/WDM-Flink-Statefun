""" Asynchronous web server with aiohttp and kafka-aio"""

# main async web server
from aiohttp import web
import asyncio

# Messages exchanged with the stateful functions
from users_pb2 import CreateUserRequest, UserRequest, UserResponse

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
USER_TOPIC = "users"
USER_CREATION_TOPIC = "users-create"
USER_EVENTS_TOPIC = "user-events"

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
            resp = UserResponse()
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
            consumer.stop()
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
            time.sleep(4)
            producer.stop()
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

    # set the worker id
    request.worker_id = WORKER_ID
    request.request_id = str(uuid.uuid4())

    k = str(key).encode('utf-8')
    v = request.SerializeToString()

    # create a future and put it in the future messages dict
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    # add that future
    # the future will be set later by the kafka consumer
    messages[request.request_id] = fut

    await app['producer'].send_and_wait(topic, key=k, value=v)

    try:
        # Wait for the future
        result = await asyncio.wait_for(fut, timeout=TIMEOUT)

        # once we get the result (a json) delete the entry and return
        del messages[request.request_id]
        return result

    except asyncio.TimeoutError:
        logger.error('Timeout while waiting for message')

        # clean the entry and raise
        del messages[request.request_id]
        raise


# Declaration of the user endpoints
@routes.post('/users/create')
async def create_user(request):
    """ Sends a create user request to the cluster"""
    msg = CreateUserRequest()

    # wait for the response asynchronously
    result = await send_msg(USER_CREATION_TOPIC, key="create", request=msg)

    return web.Response(text=result, content_type='application/json')


@routes.delete('/users/remove/{user_id}')
async def remove_user(request):
    """ Sends a remove user request to the statefun cluster"""

    user_id = int(request.match_info['user_id'])

    msg = UserRequest()
    msg.remove_user.id = user_id

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    # return code 200 or 404 in case of success or failure
    r_json = json.loads(result)
    raise web.HTTPOk() if r_json['result'] == 'success' else web.HTTPNotFound()


@routes.get('/users/find/{user_id}')
async def find_user(request):

    user_id = int(request.match_info['user_id'])

    msg = UserRequest()
    msg.find_user.id = user_id

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    return web.Response(text=result, content_type='application/json')


@routes.get('/users/credit/{user_id}')
async def get_credit(request):
    # this can do the same as the find user as long as
    # we just return the number only

    # we get the result that is a dict of {'id': 0,
    #                                       ' credit': 100}
    # and we need to extract the credit from there and return it
    response: web.Response = await find_user(request)

    r_json = json.loads(response.text)

    return web.Response(
        text=json.dumps({'credit': r_json['credit']}),
        content_type='application/json'
    )


@routes.post('/users/credit/subtract/{user_id}/{amount}')
async def subtract_credit(request):

    user_id = int(request.match_info['user_id'])
    amount = int(request.match_info['amount'])

    msg = UserRequest()
    msg.subtract_credit.id = user_id
    msg.subtract_credit.amount = amount

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    # return code 200 or 404 in case of success or failure
    r_json = json.loads(result)
    raise web.HTTPOk(
    ) if r_json['result'] == 'success' else web.HTTPBadRequest()


@routes.post('/users/credit/add/{user_id}/{amount}')
async def add_credit(request):

    user_id = int(request.match_info['user_id'])
    amount = int(request.match_info['amount'])

    msg = UserRequest()
    msg.add_credit.id = user_id
    msg.add_credit.amount = amount

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    # return code 200 or 404 in case of success or failure
    r_json = json.loads(result)
    raise web.HTTPOk(
    ) if r_json['result'] == 'success' else web.HTTPBadRequest()



# create the application object and add routes
app = web.Application()
app.add_routes(routes)

# add the background tasks
app.on_startup.append(create_kafka_producer)
app.on_startup.append(create_kafka_consumer)

# add the shutdown tasks
app.on_cleanup.append(shutdown_kafka)


if __name__ == "__main__":
    web.run_app(app)
