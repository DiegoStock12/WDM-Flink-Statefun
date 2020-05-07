from kafka import KafkaProducer
from kafka import KafkaConsumer

from sys import argv

from example_pb2 import IncreaseUserCount, ExampleRequest

KAFKA_BROKER = "localhost:9092"

function = str(argv[1])

if function == "name":
    name = str(argv[2])
    print("Received request to increment name ",name)
    request = IncreaseUserCount()
    request.name = name

    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

    key = name.encode('utf-8')
    val = request.SerializeToString()
    producer.send(topic="names", key=key, value=val)
    producer.flush()

elif function == "test":
    request = ExampleRequest()
    request.message = "Hola!!!"

    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

    key = "test".encode('utf-8')
    val = request.SerializeToString()
    producer.send(topic="test", key=key, value=val)
    producer.flush()

elif function == 'consume':
    print("Starting consumer")
    consumer = KafkaConsumer(
        'greetings', 
        bootstrap_servers = [KAFKA_BROKER], 
        auto_offset_reset='earliest',
        group_id = 'api-endp'
    )

    while True:
        for msg in consumer:
            print(msg)

