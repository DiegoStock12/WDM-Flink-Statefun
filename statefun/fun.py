""" File including the functions served by the endpoint """
import typing
import logging

from example_pb2 import IncreaseUserCount, User, ExampleRequest, ExampleResponse
from users_pb2 import CreateUserRequest, CreateUserResponse
from users_pb2 import FindUserRequest, AddCreditRequest, SubtractCreditRequest, RemoveUserRequest
from users_pb2 import AddCreditResponse, SubtractCreditResponse
from users_pb2 import UserRequest

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
def create_user(context, request: CreateUserRequest):
    """ Creates a user by sending a message to the user function 
    - Only has one state (int) that saves the current id to be 
    asigned to the next user """

    logger.info("Creating user...")

    # get the current id to assign
    state = context.state('count').unpack(Count)
    if not state:
        logger.info("First user ever!")
        state = Count()
        state.num = 0

    # send a message to the user function to define the user
    request = CreateUserWithId()
    request.id = state.num
    print(f"Sending request to function with id {request.id}", flush=True)
    context.pack_and_send("users/user", str(request.id), request)

    # update the next id to assign and save
    state.num += 1
    context.state('count').pack(state)
    logger.info('Next state to assign is {}'.format(state.num))


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
    state = context.state('user').unpack(UserData)

    response = None

    # depending on the message do one thing or the other
    if isinstance(request, UserRequest):
        logger.info("Received user request!")
        
        # check which field we have
        msg_type = request.WhichOneof('message')
        logger.info(f'Got message of type {msg_type}')

        if msg_type == 'find_user':
            logger.info('finding user')
            response = state
            logger.info(f'Found user: {response.id}:{response.credit}')
        
        elif msg_type == 'remove_user':
            logger.info(f"Deleting user {request.remove_user.id}")
            del context['user']

        elif  msg_type == 'add_credit':
            # Update the credit and save state
            state.credit += request.add_credit.amount
            context.state('user').pack(state)

            # Send the response
            response = AddCreditResponse()
            response.result = "success"

            logger.info(f"New credit for user {request.add_credit.id} is {state.credit}")

        elif msg_type == 'subtract_credit':
            # try to subtract the amount from the user credit
            new_amount = state.credit - request.subtract_credit.amount
            response = SubtractCreditResponse()
            
            if new_amount >= 0:
                state.credit -= request.subtract_credit.amount
                context.state('user').pack(state)

                response.result = "success"
                logger.info(f"New credit for user {request.subtract_credit.id} is {state.credit}")
            
            else:
                response.result = "failure"
                logger.info('Failure updating credit')

    elif isinstance(request, CreateUserWithId):
        # create a new user with the id given and 0 credit
        state = UserData()
        state.id = request.id
        state.credit = 0
        context.state('user').pack(state)
        logger.info(f'Created new user with id {request.id}')
    
    else:
        logger.error('Received unknown message type!')

    # respond if needed
    if response: 
        egress_message = kafka_egress_record(
            topic = USER_EVENTS_TOPIC, 
            key= "example".encode('utf-8'), 
            value=response
            )
        context.pack_and_send_egress("users/out", egress_message)


@functions.bind("example/increment")
def increment_user(context, request: IncreaseUserCount):
    state = context.state('user').unpack(User)
    if not state:
        print(f"First time I see this user {request.name}", flush=True)
        state = User()
        state.count = 1
    else:
        state.count += 1
    context.state('user').pack(state)

    print(f"Current number for user {request.name} is {state.count}", flush=True)

    # send it to the exit topic
    response = compute_response(name= request.name)
    egress_message = kafka_egress_record(topic='greetings', key=request.name, value=response)
    context.pack_and_send_egress("example/greets", egress_message)
    print(f"Sent message {response} to topic greetings", flush=True)

def compute_response(name):
    response = ExampleResponse()
    response.message = "Hello! This is a response for user {}".format(name)
    return response

@functions.bind("example/request")
def send_request(context, msg : typing.Union[ExampleRequest, ExampleResponse]):
    if isinstance(msg, ExampleRequest):
        print("Got a new request!, Sending message to other function", flush=True)
        m = ExampleRequest()
        m.message = msg.message
        context.pack_and_send("example/reply", "id", m)
    
    elif isinstance(msg, ExampleResponse):
        print(f"Got an example response with message {msg.message}", flush =True)

@functions.bind("example/reply")
def send_reponse(context, msg: ExampleRequest):
    print(f"Got a message: {msg.message} replying...", flush =True)
    m = ExampleResponse()
    m.message = "repliying to you from example/reply"
    context.pack_and_reply(m)


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


