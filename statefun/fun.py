""" File including the functions served by the endpoint """
import typing
import logging
import json

from users_pb2 import CreateUserRequest
from users_pb2 import UserRequest, UserResponse

# to be used internally as state or message from 
# one function to the other
from users_pb2 import UserData, Count, CreateUserWithId

from statefun import StatefulFunctions
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

USER_EVENTS_TOPIC = "user-events"

functions = StatefulFunctions()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()


# Functions to deal with user management

# Function to create users
# extracts the next free user id from its state and 
# sends a creation request to that new user function
@functions.bind("users/create")
def create_user(context, create_user_request : CreateUserRequest):
    """ Creates a user by sending a message to the user function 
    - Only has one state (int) that saves the current id to be 
    asigned to the next user """

    logger.debug("Creating user...")

    # get the current id to assign
    state = context.state('count').unpack(Count)
    if not state:
        logger.debug("First user ever!")
        state = Count()
        state.num = 0

    # send a message to the user function to define the user
    # also send the request and worker id with it
    request = CreateUserWithId()
    request.id = state.num
    request.request_id =  create_user_request.request_id
    request.worker_id = create_user_request.worker_id

    logger.debug(f"Sending request to function with id {request.id}")
    context.pack_and_send("users/user", str(request.id), request)

    # update the next id to assign and save
    state.num += 1
    context.state('count').pack(state)
    logger.debug('Next state to assign is {}'.format(state.num))


# Managing the user finding and credit management operations
# The function holds a UserData() object as its state and updates everything
# there
@functions.bind("users/user")
def operate_user(context,
                 request: typing.Union[UserRequest, CreateUserWithId]):
    """ Does all the operations with a single user

    Has the state of a user in a UserData() object that includes
    its id and credit under the name 'user' """

    # Get the current state for a given user
    # could have to handle the state not existing for this user
    state: UserData = context.state('user').unpack(UserData)

    response = None

    # depending on the message do one thing or the other
    if isinstance(request, UserRequest):
        logger.debug("Received user request!")

        # check which field we have
        msg_type = request.WhichOneof('message')
        logger.debug(f'Got message of type {msg_type}')

        if msg_type == 'find_user':
            logger.debug('finding user')

            logger.debug(f'Found user: {state.id}:{state.credit}')

            response = UserResponse()
            response.result = json.dumps({'id': state.id,
                                          'credit': state.credit})

        elif msg_type == 'remove_user':
            logger.debug(f"Deleting user {request.remove_user.id}")
            del context['user']

            response = UserResponse()
            response.result = json.dumps({'result': 'success'})

        elif msg_type == 'add_credit':
            # Update the credit and save state
            state.credit += request.add_credit.amount
            context.state('user').pack(state)

            logger.debug(f"New credit for user {request.add_credit.id} is {state.credit}")

            # send the reponse
            response = UserResponse()
            response.result = json.dumps({'result': 'success'})

        elif msg_type == 'subtract_credit':
            # try to subtract the amount from the user credit
            new_amount = state.credit - request.subtract_credit.amount
            response = UserResponse()

            if new_amount >= 0:
                state.credit -= request.subtract_credit.amount
                context.state('user').pack(state)

                # response.result = "success"
                logger.debug(f"New credit for user {request.subtract_credit.id} is {state.credit}")

                response.result = json.dumps({'result': 'success'})

            else:
                response.result = json.dumps({'result': 'failure'})
                logger.debug('Failure updating credit')

    elif isinstance(request, CreateUserWithId):
        # create a new user with the id given and 0 credit
        state = UserData()
        state.id = request.id
        state.credit = 0
        context.state('user').pack(state)
        logger.debug(f'Created new user with id {request.id}')

        response = UserResponse()
        response.result = json.dumps({'id': state.id})

    else:
        logger.error('Received unknown message type!')

    # respond if needed
    if response:
        # Use the same request id in the message body
        # and use the request worker_id as key of the message

        response.request_id = request.request_id
        logger.debug(f'Sending response {response} with key {request.worker_id}')

        # create the egress message and send it to the 
        # users/out egress
        egress_message = kafka_egress_record(
            topic=USER_EVENTS_TOPIC,
            key=request.worker_id,
            value=response
        )

        logger.debug(f'Created egress message: {egress_message}')

        context.pack_and_send_egress("users/out", egress_message)


# Use the handler and expose the endpoint
handler = RequestReplyHandler(functions)

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/statefun', methods=['POST'])
def handle():
    response_data = handler(request.data)
    response = make_response(response_data)
    response.headers.set('Content-Type', 'application/octet-stream')
    return response


@app.route('/')
def welcome():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
