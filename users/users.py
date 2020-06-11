""" File including the functions served by the endpoint """
from flask import Flask, request, make_response
import typing
import logging
import json

# Messages and internal states of the functions
from users_pb2 import CreateUserRequest, UserRequest, UserData

# messages from the payment service
from users_pb2 import UserPayRequest, UserPayResponse, UserCancelPayRequest

# Import the general response message
from general_pb2 import ResponseMessage

# import the basic statefun members
from statefun import StatefulFunctions
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

# Logging config
FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()

# Topic to output the responses to
USER_EVENTS_TOPIC = "user-events"

# Functions where to bind
functions = StatefulFunctions()

def copy_request_info(origin, destination):
    """ Copies the request_info field of two messages"""
    destination.request_info.request_id = origin.request_info.request_id
    destination.request_info.worker_id = origin.request_info.worker_id
    return destination


# Managing the user finding and credit management operations
# The function holds a UserData() object as its state and updates everything
# there
@functions.bind("users/user")
def operate_user(context,
                 request: typing.Union[UserPayRequest, UserCancelPayRequest,
                                       UserRequest, CreateUserRequest]):
    """ Does all the operations with a single user

    Has the state of a user in a UserData() object that includes
    its id and credit under the name 'user' """

    # Get the current state for a given user
    # could have to handle the state not existing for this user
    state: UserData = context.state('user').unpack(UserData)

    response = None

    # ----------------------------------------
    # Messages from the payment endpoint
    # ----------------------------------------

    if isinstance(request, UserPayRequest):

        #logger.debug('Received request to decrement user credit')
        # calculate if the credit is enough to pay for the product
        # get the credit
        response = UserPayResponse()
        response.order_id = request.order_id

        # copy the information of the request_info
        response = copy_request_info(request, response)

        # if the user exists then do the checks
        if state:
            # see whether we should return success or failure
            if state.credit - request.amount < 0:
                response.success = False
            else:
                state.credit -= request.amount
                response.success = True

        else:
            response.success = False

        # pack the state
        context.state('user').pack(state)

        # respond to the payment service
        context.pack_and_reply(response)
        return


    elif isinstance(request, UserCancelPayRequest):

        #logger.debug('Received request to cancel a payment')
        # add the amount specified to the user credit
        response = UserPayResponse()
        response.order_id = request.order_id

        # copy the information
        response = copy_request_info(request, response)

        if state:
            state.credit += request.amount
            # reply
            response.success = True

        else:
            response.success = False

        # pack the state
        context.state('user').pack(state)

        # reply to the sender function
        context.pack_and_reply(response)
        return

    # -------------------------------------
    # Interaction with the user endpoint
    # -------------------------------------

    elif isinstance(request, CreateUserRequest):
        # we are given the uuid in the message so that's already done
        state = UserData()
        state.id = request.id
        state.credit = 0

        #logger.debug(f'Created new user with id {request.id}')
        context.state('user').pack(state)

        response = ResponseMessage()
        response.result = json.dumps({'user_id': state.id})

    elif isinstance(request, UserRequest):

        # check which field we have
        msg_type = request.WhichOneof('message')
        #logger.debug(f'Got message of type {msg_type}')

        # If the state is None we return an error
        if not state:
            response = ResponseMessage()
            response.result = json.dumps({'result': 'failure: user does not exist'})

        else:
            # If the state exists we then operate with it
            if msg_type == 'find_user':

                response = ResponseMessage()
                response.result = json.dumps({'user_id': state.id,
                                              'credit': state.credit})
                # pack the state
                context.state('user').pack(state)

            elif msg_type == 'remove_user':
                del context['user']

                response = ResponseMessage()
                response.result = json.dumps({'result': 'success'})

            elif msg_type == 'add_credit':
                # Update the credit and save state
                state.credit += request.add_credit.amount
                context.state('user').pack(state)


                # send the response
                response = ResponseMessage()
                response.result = json.dumps({'result': 'success'})

            elif msg_type == 'subtract_credit':
                # try to subtract the amount from the user credit
                new_amount = state.credit - request.subtract_credit.amount
                response = ResponseMessage()

                if new_amount >= 0:
                    state.credit -= request.subtract_credit.amount
                    context.state('user').pack(state)

                    response.result = json.dumps({'result': 'success'})

                else:
                    response.result = json.dumps({'result': 'failure'})

    else:
        #logger.error('Received unknown message type!')

    # respond if needed
    if response:
        # Use the same request id in the message body
        # and use the request worker_id as key of the message

        response.request_id = request.request_info.request_id

        # create the egress message and send it to the
        # users/out egress
        egress_message = kafka_egress_record(
            topic=USER_EVENTS_TOPIC,
            key=request.request_info.worker_id,
            value=response
        )

        context.pack_and_send_egress("users/out", egress_message)


# Use the handler and expose the endpoint
handler = RequestReplyHandler(functions)

app = Flask(__name__)


@app.route('/statefun', methods=['POST'])
def handle():
    response_data = handler(request.data)
    response = make_response(response_data)
    response.headers.set('Content-Type', 'application/octet-stream')
    return response


if __name__ == "__main__":
    app.run()