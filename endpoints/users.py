from flask import Flask, jsonify

# Import the messages to be sent to the statefun cluster
from users_pb2 import CreateUserRequest
from users_pb2 import UserRequest, UserResponse

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable

import threading
import time
import uuid

app = Flask(__name__)

KAFKA_BROKER = "kafka-broker:9092"
USER_TOPIC = "users"
USER_CREATION_TOPIC = "users-create"

USER_EVENTS_TOPIC = "user-events"

brokers_available = False
producer = None

new_messages = {}

while not brokers_available:
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        consumer = KafkaConsumer(
            'user-events',
            bootstrap_servers=[KAFKA_BROKER],
            auto_offset_reset='earliest',
        )
        brokers_available = True
        print("Got the broker!", flush=True)
    except NoBrokersAvailable:
        time.sleep(4)
        continue


def consume_forever(cons: KafkaConsumer):
    print('Strated consumer thread', flush=True)
    for msg in cons:
        print(f'Received message! {msg.value}', flush=True)
        resp = UserResponse()
        resp.ParseFromString(msg.value)
        new_messages[resp.request_id] = resp.result


con_thread = threading.Thread(target=consume_forever, args=[consumer])
con_thread.start()


# ENDPOINTS OF THE USER API

def get_message(id: str):
    """ Returns a given message from the dictionary"""

    result = None
    while id not in new_messages:
        print("Not found the message", flush=True)
        time.sleep(0.2)
    if id in new_messages:
        result = new_messages[id]
        del new_messages[id]

    return result


@app.route('/users/create', methods=['POST'])
def create_user():
    """ Sends a create user request to the cluster"""
    request = CreateUserRequest()
    request.request_id = str(uuid.uuid4())

    send_msg(USER_CREATION_TOPIC, key="create", request=request)

    result = get_message(request.request_id)

    return jsonify(result)


@app.route('/users/remove/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    """ Sends a remove user request to the statefun cluster"""
    request = UserRequest()
    request.remove_user.id = user_id
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return jsonify(result)



@app.route('/users/find/<int:user_id>', methods=['GET'])
def find_user(user_id):
    """ Searches for a user in the cluster """
    request = UserRequest()
    request.find_user.id = user_id
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return jsonify(result)



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
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)
    result = get_message(request.request_id)

    return jsonify(result)



@app.route('/users/credit/add/<int:user_id>/<int:amount>', methods=['POST'])
def add_credit(user_id, amount):
    request = UserRequest()
    request.add_credit.id = user_id
    request.add_credit.amount = amount
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return jsonify(result)


def send_msg(topic, key, request):
    """ Sends a protobuf message to the specified topic"""
    global producer

    k = str(key).encode('utf-8')
    v = request.SerializeToString()

    producer.send(topic=topic, key=k, value=v)


@app.route('/')
def basic():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
