""" File including the functions served by the endpoint """
import logging
import typing
import json

from orders_pb2 import Order, CreateOrder, CreateOrderWithId, CreateOrderResponse, OrderRequest, OrderResponse
from users_pb2 import Count

from google.protobuf.json_format import MessageToJson

from statefun import StatefulFunctions, RequestReplyHandler, kafka_egress_record

functions = StatefulFunctions()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()

ORDER_EVENTS_TOPIC = "order-events"


@functions.bind("orders/create")
def create_order(context, msg: CreateOrder):
    """ Creates an order by sending a message to the order function 
    - Only has one state (int) that saves the current id to be 
    assigned to the next order """

    logger.info("Creating order...")

    # get the current id to assign
    state = context.state('count').unpack(Count)

    if not state:
        state = Count()
        state.num = 0

    request = CreateOrderWithId()
    request.id = state.num
    request.userId = msg.userId
    request.worker_id = msg.worker_id
    print(f"Sending request to function with id {request.id}", flush=True)
    context.pack_and_send("orders/order", str(request.id), request)

    # update the next id to assign and save
    state.num += 1
    context.state('count').pack(state)
    logger.info('Next state to assign is {}'.format(state.num))


@functions.bind("orders/order")
def operate_order(context, msg: typing.Union[CreateOrderWithId, OrderRequest]):
    """ Does all the operations with a single order """
    response = None

    if isinstance(msg, CreateOrderWithId):
        state = Order()
        state.id = msg.id
        state.userId = msg.user_id

        context.state('order').pack(state)
        logger.info(f'Created new order with id {msg.id}')

        response = OrderResponse()
        response.result = json.dumps({'order_id': state.id})

    elif isinstance(msg, OrderRequest):
        logger.info("Received order request!")

        msg_type = msg.WhichOneof('message')
        logger.info(f'Got message of type {msg_type}')

        if msg_type == 'remove_order':
            state = context.state('order').unpack(Order)
            if not state:
                logger.info("Order does not exists.")
                response = OrderResponse()
                response.result = json.dumps({'result': 'failure', 'message': 'Order does not exist.'})
            else:
                logger.info(f"Deleting the order with id: {msg.remove_order.id}")
                del context['order']
                response = OrderResponse()
                response.result = json.dumps({'result': 'success'})

        elif msg_type == 'find_order':
            state = context.state('order').unpack(Order)
            if not state:
                logger.info("Order does not exist.")
                response = OrderResponse()
                response.result = json.dumps({'result': 'failure', 'message': 'Order does not exist.'})
            else:
                logger.info(f"{state}")
                logger.info(f"Returning order with id: {msg.find_order.id}")
                response.result = MessageToJson(state)

        elif msg_type == 'add_item':
            state = context.state('order').unpack(Order)
            if not state:
                logger.info("Order does not exist.")
                response.result = json.dumps({'result': 'failure', 'message': 'Order does not exist.'})
            else:
                state.items.append(msg.add_item.itemId)
                logger.info(f"{state}")
                context.state('order').pack(state)
                logger.info(f"Returning order with id: {msg.add_item.id}")
                response.result = json.dumps({'result': 'success'})


        elif msg_type == 'remove_item':
            orderId = msg.remove_item.id
            state = context.state('order').unpack(Order)
            if not state:
                logger.info("Order does not exist.")
            else:
                items = state.items
                logger.info(f"{type(items)}")
                logger.info(f"{len(items)}")
                item_to_delete = msg.remove_item.itemId
                item_index = -1
                for i in range(len(items)):
                    logger.info(f"{items[i]}")
                    if items[i] == item_to_delete:
                        item_index = i
                if item_index != -1:
                    del state.items[item_index]
                    logger.info(f"Removing item {item_to_delete} from order {orderId}")
                    response.result = json.dumps({'result': 'success'})
                else:
                    logger.info(f"Order {orderId} does not contain item with id {item_to_delete}")
                    response.result = json.dumps({'result': 'failure',
                                                  'message': 'Order does not contain requested item.'})

                context.state('order').pack(state)

    else:
        logger.error('Received unknown message type!')

    if response:
        logger.info("Sending a response.")
        egress_message = kafka_egress_record(
            topic=ORDER_EVENTS_TOPIC,
            key=msg.worker_id,
            value=response
            )
        context.pack_and_send_egress("orders/out", egress_message)


# Use the handler and expose the endpoint
handler = RequestReplyHandler(functions)

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/statefun', methods=['POST'])
def handle():
    response_data = handler(request.data)
    response = make_response(response_data)
    response.headers.set('Content-Type', 'application/octet-stream')
    return response


@app.route('/')
def welcome():
    return "This is Orders microservice!"


if __name__ == "__main__":
    app.run()


