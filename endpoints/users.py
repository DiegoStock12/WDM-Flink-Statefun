from flask import Flask, Response

# Import the messages to be sent to the statefun cluster
from users_pb2 import CreateUserRequest, UserRequest, UserResponse

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable

import threading
import time
import uuid
import json

from typing import Dict

# create the logger and configure
import logging

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"
USER_TOPIC = "users"
USER_CREATION_TOPIC = "users-create"
USER_EVENTS_TOPIC = "user-events"

brokers_available = False
producer = None

# Where yet to answer request messages
# are kept
new_messages: Dict[str, str] = {}

# The worker id that we'll use to identify
# messages adderessed to us
WORKER_ID: str = str(uuid.uuid4())
logger.info(f'Started worker with id {WORKER_ID}')


# Get the global
while not brokers_available:
    try:
        # Try to create the producer and consumer for
        # this worker
        producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
        consumer = KafkaConsumer(
            USER_EVENTS_TOPIC,
            bootstrap_servers=[KAFKA_BROKER],
            auto_offset_reset='latest',
        )
        brokers_available = True
        logger.info('Got the broker!')
    except NoBrokersAvailable:
        time.sleep(2)
        continue


# Background thread receiving messages from
# the kafka topic and putting them in the dictionary
def consume_forever(cons: KafkaConsumer):
    logger.info('Started consumer thread')
    for msg in cons:
        if msg.key.decode('utf-8') == WORKER_ID:
            logger.info(f'Received message! {msg.value}')
            resp = UserResponse()
            resp.ParseFromString(msg.value)
            new_messages[resp.request_id] = resp.result


# Create and start the background thread for the consumer
con_thread = threading.Thread(target=consume_forever, args=[consumer])
con_thread.start()


# Looks for the message in the local dict
def get_message(id: str):
    """ Returns a given message from the dictionary"""
    logger.info(new_messages)

    result = None
    while id not in new_messages:
        logger.info("Not found the message")
        logger.info(new_messages)

        # TODO we have to tweak this time based 
        # on real-world performance
        time.sleep(0.02)

    # Once the message is present return and delete it
    result = new_messages[id]
    del new_messages[id]

    return result


# Create the flask app
app = Flask(__name__)


# ENDPOINTS OF THE USER API
@app.route('/users/create', methods=['POST'])
def create_user():
    """ Sends a create user request to the cluster"""
    request = CreateUserRequest()
    request.request_id = str(uuid.uuid4())

    send_msg(USER_CREATION_TOPIC, key="create", request=request)

    result = get_message(request.request_id)

    return Response(result, mimetype='application/json')


@app.route('/users/remove/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    """ Sends a remove user request to the statefun cluster"""
    request = UserRequest()
    request.remove_user.id = user_id
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return Response(result, mimetype='application/json')


@app.route('/users/find/<int:user_id>', methods=['GET'])
def find_user(user_id):
    """ Searches for a user in the cluster """
    request = UserRequest()
    request.find_user.id = user_id
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return Response(result, mimetype='application/json')


@app.route('/users/credit/<int:user_id>', methods=['GET'])
def get_credit(user_id):
    # this can do the same as the find user as long as
    # we just return the number only

    # we get the result that is a dict of {'id': 0,
    #                                       ' credit': 100}
    # and we need to extract the credit from there and return it
    result: Response = find_user(user_id)

    r_json = json.loads(result.data)

    return Response(json.dumps({'credit': r_json['credit']}), mimetype='application/json')


@app.route('/users/credit/subtract/<int:user_id>/<int:amount>', methods=['POST'])
def subtract_credit(user_id, amount):
    request = UserRequest()
    request.subtract_credit.id = user_id
    request.subtract_credit.amount = amount
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return Response(result, mimetype='application/json')


@app.route('/users/credit/add/<int:user_id>/<int:amount>', methods=['POST'])
def add_credit(user_id, amount):
    request = UserRequest()
    request.add_credit.id = user_id
    request.add_credit.amount = amount
    request.request_id = str(uuid.uuid4())

    send_msg(USER_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return Response(result, mimetype='application/json')


def send_msg(topic, key, request):
    """ Sends a protobuf message to the specified topic"""

    # Add the worker id to all requests
    request.worker_id = WORKER_ID

    k = str(key).encode('utf-8')
    v = request.SerializeToString()

    producer.send(topic=topic, key=k, value=v)

    # If we don't have a lot of messages 
    # this really increases performance
    producer.flush()


if __name__ == "__main__":
    app.run()
