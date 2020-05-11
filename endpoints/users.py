from flask import Flask, jsonify

from example_pb2 import IncreaseUserCount, ExampleResponse
from orders_pb2 import CreateOrder, OrderRequest

# Import the messages to be sent to the statefun cluster
from users_pb2 import CreateUserRequest, CreateUserResponse
from users_pb2 import RemoveUserRequest, RemoveUserResponse
from users_pb2 import FindUserRequest
from users_pb2 import SubtractCreditRequest, SubtractCreditResponse
from users_pb2 import AddCreditRequest, AddCreditResponse
from users_pb2 import UserRequest

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable

import threading
import time

app = Flask(__name__)

KAFKA_BROKER = "kafka-broker:9092"
USER_TOPIC = "users"
USER_CREATION_TOPIC = "users-create"


brokers_available = False
producer = None

while not brokers_available:
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        consumer = KafkaConsumer(
                'greetings', 
                bootstrap_servers = [KAFKA_BROKER], 
                auto_offset_reset='earliest'
            )
        brokers_available = True
        print("Got the broker!", flush=True)
    except NoBrokersAvailable:
        time.sleep(4)
        continue


# ENDPOINTS OF THE USER API

@app.route('/users/create', methods=['POST'])
def create_user():
    """ Sends a create user request to the cluster"""
    request = CreateUserRequest()

    send_msg(USER_CREATION_TOPIC, key="create", value = request)
    return "User create"


@app.route('/users/remove/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    """ Sends a remove user request to the statefun cluster"""
    request = UserRequest()
    request.remove_user.id = user_id

    send_msg(USER_TOPIC, key=user_id, value = request)
    return "User remove"


@app.route('/users/find/<int:user_id>', methods=['GET'])
def find_user(user_id):
    """ Searches for a user in the cluster """
    request = UserRequest()
    request.find_user.id = user_id

    send_msg(USER_TOPIC, key=user_id, value = request)
    return "User find"

@app.route('/users/credit/<int:user_id>', methods=['GET'])
def get_credit(user_id):
    # this can do the same as the find user as long as 
    # we just return the number only
    find_user(user_id)

    # Here we should get the response and extract the credit 
    # instead of the whole user

@app.route('/users/credit/subtract/<int:user_id>/<int:amount>', methods=['POST'])
def subtract_credit(user_id, amount):
    
    request = UserRequest()
    request.subtract_credit.id = user_id
    request.subtract_credit.amount = amount

    send_msg(USER_TOPIC, key=user_id, value=request)
    return "User subtract"

@app.route('/users/credit/add/<int:user_id>/<int:amount>', methods=['POST'])
def add_credit(user_id, amount):
    
    request = UserRequest()
    request.add_credit.id = user_id
    request.add_credit.amount = amount
    
    send_msg(USER_TOPIC, key=user_id, value=request)
    return "User add"


def send_msg(topic, key, value):
    """ Sends a protobuf message to the specified topic"""
    global producer 

    k = str(key).encode('utf-8')
    v = value.SerializeToString()

    producer.send(topic=topic, key= k, value = v)



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


@app.route('/orders/create/<int:userId>', methods=['POST'])
def create_order(userId):
    global producer, consumer

    print("Received request to create order for user", flush=True)
    request = CreateOrder()
    request.userId = userId

    if producer is None:
        print("Creating the producer", flush=True)
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        print("Got the broker!", flush=True)

    send_msg("orders-create", "create_order", request)

    return jsonify({'response': 'Created order'})


@app.route('/orders/remove/<int:orderId>', methods=['DELETE'])
def remove_order(orderId):
    global producer, consumer

    print("Received request to remove order.", flush=True)
    request = OrderRequest()
    request.remove_order.id = orderId

    if producer is None:
        print("Creating the producer", flush=True)
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        print("Got the broker!", flush=True)

    send_msg("orders", orderId, request)

    return jsonify({'response': 'Removed order'})


@app.route('/orders/find/<int:orderId>', methods=['GET'])
def get_order(orderId):
    global producer, consumer

    print("Received request to find an order.", flush=True)
    request = OrderRequest()
    request.find_order.id = orderId

    if producer is None:
        print("Creating the producer", flush=True)
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        print("Got the broker!", flush=True)

    send_msg("orders", orderId, request)

    return jsonify({'response': 'Found order'})

@app.route('/test/<string:name>')
def test(name):
    return f"It's working {name}!!"

@app.route('/')
def basic():
    return "Hello world!"
    

if __name__ == "__main__":
    app.run()
