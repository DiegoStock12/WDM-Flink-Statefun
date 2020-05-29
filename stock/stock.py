""" File including the functions served by the endpoint """
from flask import Flask, request, jsonify, make_response
import typing
import logging
import json

from stock_pb2 import *
from general_pb2 import ResponseMessage

from statefun import StatefulFunctions
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

functions = StatefulFunctions()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()

# Topic to output the responses to
STOCK_EVENTS_TOPIC = "stock-events"

# Functions to deal with stock management

# Function to create stock
# Extracts the next free stock id from its state and
# Sends a creation request to that new user function
@functions.bind("stock/create")
def create_item(context, request: CreateItemRequest):
    """ Creates an item by sending a message to the user function
    - Only has one state (int) that saves the current id to be
    asigned to the next user """

    logger.info("Creating item...")

    # get the current id to assign
    state = context.state('count').unpack(Count)
    if not state:
        state = Count()
        state.num = 0

    item_request = CreateItemWithId()
    item_request.id = state.num
    item_request.price = request.price
    item_request.request_id = request.request_id
    item_request.worker_id = request.worker_id
    print(f"Sending request to function with id {item_request.id}", flush=True)
    context.pack_and_send("stock/stock", str(item_request.id), item_request)

    # update the next id to assign and save
    state.num += 1
    context.state('count').pack(state)
    logger.info('Next state to assign is {}'.format(state.num))

@functions.bind("stock/stock")
def manage_stock(context, request: typing.Union[StockRequest, CreateItemWithId]):
    # Get the current state.
    item_state: ItemData = context.state('item').unpack(ItemData)

    if isinstance(request, CreateItemWithId):
        item_state = ItemData()
        item_state.id = request.id
        item_state.price = request.price
        item_state.stock = 0

        context.state('item').pack(item_state)
        logger.debug(f'Created new item with id {request.id}')

        response = ResponseMessage()
        response.result = json.dumps({'item_id': item_state.id})
    elif item_state is None:
        # Item does not exist yet. Return error.
        response = ResponseMessage()
        response.result = json.dumps({'result:': 'not_found'})
    elif isinstance(request, StockRequest):
        logger.debug("Received stock request!")

        # check which field we have
        msg_type = request.WhichOneof('message')
        logger.debug(f'Got message of type {msg_type}')

        if msg_type == "find_item":
            response = ResponseMessage()
            response.result = json.dumps({'id:': item_state.id, 'price': item_state.price, 'stock': item_state.stock})
        elif msg_type == "subtract_stock":
            new_amount = item_state.stock - request.subtract_stock.amount
            response = ResponseMessage()

            if new_amount >= 0:
                item_state.stock -= request.subtract_stock.amount

                context.state('item').pack(item_state)
                response.result = json.dumps({'result': 'success', 'item_id': item_state.id})
            else:
                response.result = json.dumps({'result': 'stock too low', 'item_id': item_state.id})

        elif msg_type == "add_stock":
            item_state.stock += request.add_stock.amount
            context.state('item').pack(item_state)

            # send the reponse.
            response = ResponseMessage()
            response.result = json.dumps({'result': 'success', 'item_id': item_state.id})
    if response:
        # Use the same request id in the message body
        # and use the request worker_id as key of the message

        response.request_id = request.request_id
        logger.debug(
            f'Sending response {response} with key {request.worker_id}')


        if not request.internal:
            # create the egress message and send it to the
            # users/out egress
            egress_message = kafka_egress_record(
                topic=STOCK_EVENTS_TOPIC,
                key=request.worker_id,
                value=response
            )

            logger.debug(f'Created egress message: {response}')

            context.pack_and_send_egress("stock/out", egress_message)
        else:
            context.pack_and_send("orders/order", str(request.order_id), response)

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