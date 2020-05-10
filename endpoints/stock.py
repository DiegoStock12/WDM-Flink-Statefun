import time

from flask import Flask
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable

from endpoints.stock_pb2 import CreateItemRequest

app = Flask(__name__)

KAFKA_BROKER = "kafka-broker:9092"
STOCK_TOPIC = "stock"
STOCK_CREATION_TOPIC = "stock-create"

brokers_available = False
producer = None

while not brokers_available:
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        consumer = KafkaConsumer(
            'greetings',
            bootstrap_servers=[KAFKA_BROKER],
            auto_offset_reset='earliest'
        )
        brokers_available = True
        print("Got the broker!", flush=True)
    except NoBrokersAvailable:
        time.sleep(4)
        continue


# ENDPOINTS OF THE STOCK API

@app.route('/stock/item/create/<int:price>', methods=['POST'])
def create_item(price):
    """ Sends a create item request to the cluster"""
    request = CreateItemRequest()
    request.price = price

    send_msg(STOCK_TOPIC, key="create", value=request)
    return "User create"


def send_msg(topic, key, value):
    """ Sends a protobuf message to the specified topic"""
    global producer

    k = str(key).encode('utf-8')
    v = value.SerializeToString()

    producer.send(topic=topic, key= k, value = v)

if __name__ == "__main__":
    app.run()