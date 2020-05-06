from flask import Flask, jsonify

from example_pb2 import IncreaseUserCount

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

import time

app = Flask(__name__)

KAFKA_BROKER = "kafka-broker:9092"
brokers_available = False
producer = None

while not brokers_available:
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        brokers_available = True
        print("Got the broker!", flush=True)
    except NoBrokersAvailable:
        time.sleep(2)
        continue

@app.route('/user/<string:name>/add')
def increment_user(name):
    """ Sends an increment request to the specified name"""
    global producer

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

    return jsonify({'name': name})

@app.route('/test/<string:name>')
def test(name):
    return f"It's working {name}!!"

@app.route('/')
def basic():
    return "Hello world!"
    

if __name__ == "__main__":
    app.run()
