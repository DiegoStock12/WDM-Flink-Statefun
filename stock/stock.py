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



@functions.bind("stock/stock")
def manage_stock(context, request: typing.Union[StockRequest, CreateItemRequest]):
    # Get the current state.
    item_state: ItemData = context.state('item').unpack(ItemData)

    if isinstance(request, CreateItemRequest):
        item_state = ItemData()
        item_state.id = request.id
        item_state.price = request.price
        item_state.stock = 0

        context.state('item').pack(item_state)
        #logger.debug(f'Created new item with id {request.id}')

        response = ResponseMessage()
        response.result = json.dumps({'item_id': item_state.id})

    elif isinstance(request, StockRequest):

        # If the item state is None we return an error
        if item_state is None:
            # Item does not exist yet. Return error.
            if not request.internal:
                response = ResponseMessage()
                response.result = json.dumps({'result': 'not_found'})
            else:
                response = StockResponse()
                response.item_id = request.subtract_stock.id
                response.result = 'failure'

        else:
            # check which field we have
            msg_type = request.WhichOneof('message')
            #logger.debug(f'Got message of type {msg_type}')

            if msg_type == "find_item":
                response = ResponseMessage()
                response.result = json.dumps(
                    {'id:': item_state.id, 'price': item_state.price, 'stock': item_state.stock})

                context.state('item').pack(item_state)

            elif msg_type == "subtract_stock":
                new_amount = item_state.stock - request.subtract_stock.amount

                if not request.internal:
                    response = ResponseMessage()
                else:
                    response = StockResponse()

                if new_amount >= 0:
                    item_state.stock -= request.subtract_stock.amount

                    context.state('item').pack(item_state)

                    if not request.internal:
                        response.result = json.dumps({'result': 'success', 'item_id': item_state.id})
                    else:
                        # Include the item id and price
                        response.price = item_state.price
                        response.item_id = item_state.id
                        response.result = 'success'
                else:
                    if not request.internal:
                        response.result = json.dumps({'result': 'stock too low', 'item_id': item_state.id})
                    else:
                        response.price = item_state.price
                        response.item_id = item_state.id
                        response.result = 'failure'

            elif msg_type == "add_stock":
                item_state.stock += request.add_stock.amount
                context.state('item').pack(item_state)

                # send the response.
                response = ResponseMessage()
                response.result = json.dumps({'result': 'success', 'item_id': item_state.id})

    if response:
        # Use the same request id in the message body
        # and use the request worker_id as key of the message

        if not request.internal:
            response.request_id = request.request_info.request_id
            # create the egress message and send it to the
            # users/out egress
            egress_message = kafka_egress_record(
                topic=STOCK_EVENTS_TOPIC,
                key=request.request_info.worker_id,
                value=response
            )
            context.pack_and_send_egress("stock/out", egress_message)
        else:
            response.request_info.request_id = request.request_info.request_id
            response.request_info.worker_id = request.request_info.worker_id

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