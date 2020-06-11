import asyncio
from ssl import create_default_context, Purpose
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from kafka.structs import TopicPartition

ssl_context = create_default_context(Purpose.SERVER_AUTH)

CONFLUENT_KAFKA_BROKER= '***'

async def produce_and_consume():
    # Produce
    producer = AIOKafkaProducer(
        loop = asyncio.get_event_loop(),
        bootstrap_servers=CONFLUENT_KAFKA_BROKER,
        security_protocol='SASL_SSL',
        ssl_context=ssl_context,
        sasl_mechanism='PLAIN',
        sasl_plain_password='***',
        sasl_plain_username='***'
    )

    await producer.start()
    try:
        msg = await producer.send_and_wait(
            'test', b"Super Message", partition=0)
    finally:
        await producer.stop()

    consumer = AIOKafkaConsumer(
        'test',
        loop=asyncio.get_event_loop(),
        bootstrap_servers=CONFLUENT_KAFKA_BROKER,
        security_protocol='SASL_SSL',
        ssl_context=ssl_context,
        sasl_mechanism='PLAIN',
        sasl_plain_password='***',
        sasl_plain_username='***'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        await consumer.stop()


async def consume():
    consumer = AIOKafkaConsumer(
        'test',
        loop=asyncio.get_event_loop(),
        bootstrap_servers=CONFLUENT_KAFKA_BROKER,
        security_protocol='SASL_SSL',
        ssl_context=ssl_context,
        sasl_mechanism='PLAIN',
        sasl_plain_password='***',
        sasl_plain_username='***',
        auto_offset_reset='earliest'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print(
                "{}:{:d}:{:d}: key={} value={} timestamp_ms={}".format(
                    msg.topic, msg.partition, msg.offset, msg.key, msg.value,
                    msg.timestamp)
            )
    finally:
        await consumer.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(consume())
    try:
        loop.run_until_complete(task)
    finally:
        loop.run_until_complete(asyncio.sleep(0, loop=loop))
        task.cancel()
        try:
            loop.run_until_complete(task)
        except asyncio.CancelledError:
            pass