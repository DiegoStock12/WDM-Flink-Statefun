from flask import Flask, jsonify

from example_pb2 import IncreaseUserCount, ExampleResponse

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable

import threading
import time

app = Flask(__name__)

KAFKA_BROKER = "kafka-broker:9092"
brokers_available = False
producer = None

while not brokers_available:
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        consumer = KafkaConsumer(
                'greetings', 
                bootstrap_servers = [KAFKA_BROKER], 
                auto_offset_reset='earliest',
                group_id = 'api-endpoint-users'
            )
        brokers_available = True
        print("Got the broker!", flush=True)
    except NoBrokersAvailable:
        time.sleep(4)
        continue

@app.route('/user/<string:name>/add')
def increment_user(name):
    """ Sends an increment request to the specified name"""
    global producer, consumer

    print("Received request to increment name ",name)
    request = IncreaseUserCount()
    request.name = name

    if producer is None:
        print("Creating the producer", flush=True)
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        print("Got the broker!", flush=True)


    key = name.encode('utf-8')
    val = request.SerializeToString()
    producer.send(topic="names", key=key, value=val)
    producer.flush()

    # try to get the message from the consumer
    for msg in consumer:
        print(msg, flush=True)
        print(msg.key.decode('utf-8'), flush=True)
        if msg.key.decode('utf-8') == name:
            print("Got a response for the user {} --> {}".format(name, msg.value), flush=True)

            return jsonify({'response': msg.value.decode('utf-8')})

@app.route('/test/<string:name>')
def test(name):
    return f"It's working {name}!!"

@app.route('/')
def basic():
    return "Hello world!"
    

if __name__ == "__main__":
    app.run()
