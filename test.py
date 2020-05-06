from kafka import KafkaProducer

from sys import argv

from example_pb2 import IncreaseUserCount

KAFKA_BROKER = "localhost:9092"

name = str(argv[1])

print("Received request to increment name ",name)
request = IncreaseUserCount()
request.name = name

producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

key = name.encode('utf-8')
val = request.SerializeToString()
producer.send(topic="names", key=key, value=val)
producer.flush()