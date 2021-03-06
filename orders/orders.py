""" File including the functions served by the endpoint """
import logging
import typing
import json

from orders_pb2 import *
from general_pb2 import ResponseMessage
from payment_pb2 import PaymentStatus
from stock_pb2 import StockRequest, StockResponse, OrderAddItemStockRequest

from statefun import StatefulFunctions, RequestReplyHandler, kafka_egress_record

functions = StatefulFunctions()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()

ORDER_EVENTS_TOPIC = "order-events"

# item_to_price = {}


@functions.bind("orders/order")
def operate_order(context, msg: typing.Union[CreateOrder, OrderRequest, OrdersPayFind,
                                             OrderPaymentCancel, PaymentStatus, StockResponse]):
    """ Does all the operations with a single order """
    response = None

    if isinstance(msg, CreateOrder):
        response = create_order_with_id(context, msg)

    elif isinstance(msg, OrderRequest):

        msg_type = msg.WhichOneof('message')
        # logger.debug(f'Got message of type {msg_type}')

        if msg_type == 'remove_order':
            response = remove_order(context, msg)

        elif msg_type == 'find_order':
            response = find_order(context, msg)

        elif msg_type == 'add_item':
            response = add_item(context, msg)

        elif msg_type == 'remove_item':
            response = remove_item(context, msg)

        elif msg_type == 'order_checkout':
            response = order_checkout(context, msg)

    elif isinstance(msg, OrdersPayFind):
        order_payment_find(context, msg)

    elif isinstance(msg, OrderPaymentCancel):
        order_payment_cancel(context, msg)

    elif isinstance(msg, PaymentStatus):
        response = order_payment_confirm(context, msg)

    elif isinstance(msg, StockResponse):
        response = order_add_item_reply(context, msg)

    else:
        logger.error('Received unknown message type!')

    if response:
        response.request_id = msg.request_info.request_id
        egress_message = kafka_egress_record(
            topic=ORDER_EVENTS_TOPIC,
            key=msg.request_info.worker_id,
            value=response
        )
        context.pack_and_send_egress("orders/out", egress_message)


def create_order_with_id(context, msg):
    state = Order()
    state.id = msg.id
    state.user_id = msg.user_id
    state.paid = False
    state.total_cost = 0

    context.state('order').pack(state)
    #logger.debug(f'Created new order with id {msg.id}')

    response = ResponseMessage()
    response.result = json.dumps({'result': 'success',
                                  'order_id': state.id})
    return response


def remove_order(context, msg):
    state = context.state('order').unpack(Order)
    response = ResponseMessage()
    if not state:
        response.result = json.dumps({'result': 'failure', 'message': 'Order does not exist.'})
    else:
        #logger.info(f"Deleting the order with id: {msg.remove_order.id}")
        item_to_count = {}
        items = state.items
        for i in range(len(items)):
            id = items[i].item_id
            if id not in item_to_count.keys():
                item_to_count[id] = 1
            else:
                item_to_count[id] = item_to_count[id] + 1

        for id, cnt in item_to_count.items():
            add_stock_request = OrderAddItemStockRequest()
            add_stock_request.request_info.worker_id = msg.request_info.worker_id
            add_stock_request.request_info.request_id = msg.request_info.request_id
            add_stock_request.id = id
            add_stock_request.amount = cnt

            # logger.info('Sending request to add stock back.')
            context.pack_and_send("stock/stock", str(id), add_stock_request)

        # logger.info('Deleting order.')
        del context['order']
        response.result = json.dumps({'result': 'success'})

    return response


def find_order(context, msg):
    state = context.state('order').unpack(Order)
    response = ResponseMessage()
    if not state:
        response.result = json.dumps({'result': 'failure', 'message': 'Order does not exist.'})
    else:

        # Have to assign all like this so they're not casted to string
        response.result = json.dumps({'id': state.id, 'user_id': state.user_id,
                                      'items': [i.item_id for i in state.items], 'total_cost': state.total_cost,
                                      'paid': state.paid, 'intent': state.intent})

        context.state('order').pack(state)

    return response


def add_item(context, msg):
    state = context.state('order').unpack(Order)
    if not state:
        response = ResponseMessage()
        response.result = json.dumps({'result': 'failure', 'message': 'Order does not exist.'})

        return response
    else:
        # call stock service to reduce the stock
        subtract_stock_request = StockRequest()
        subtract_stock_request.request_info.worker_id = msg.request_info.worker_id
        subtract_stock_request.request_info.request_id = msg.request_info.request_id
        subtract_stock_request.subtract_stock.id = msg.add_item.itemId
        subtract_stock_request.subtract_stock.amount = 1
        subtract_stock_request.internal = True
        subtract_stock_request.order_id = state.id

        context.state('order').pack(state)

        context.pack_and_send("stock/stock", str(msg.add_item.itemId), subtract_stock_request)


def remove_item(context, msg):
    orderId = msg.remove_item.id
    state = context.state('order').unpack(Order)
    response = ResponseMessage()
    if not state:
        response.result = json.dumps({'result': 'failure',
                                      'message': 'Order does not exist.'})
    else:
        items = state.items
        item_to_delete = msg.remove_item.itemId
        item_index = -1
        for i in range(len(items)):
            #logger.info(f"{items[i].item_id}")
            if items[i].item_id == item_to_delete:
                item_index = i
        if item_index != -1:
            state.total_cost -= items[item_index].price
            del state.items[item_index]
            #logger.info(f"Removing item {item_to_delete} from order {orderId}")
            response.result = json.dumps({'result': 'success'})

            add_stock_request = StockRequest()
            add_stock_request.request_info.worker_id = msg.request_info.worker_id
            add_stock_request.request_info.request_id = msg.request_info.request_id
            add_stock_request.add_stock.id = item_to_delete
            add_stock_request.add_stock.amount = 1

            context.pack_and_send("stock/stock", str(item_to_delete), add_stock_request)

        else:
            #logger.warning(f"Order {orderId} does not contain item with id {item_to_delete}")
            response.result = json.dumps({'result': 'failure',
                                          'message': 'Order does not contain requested item.'})

        context.state('order').pack(state)

    return response


def order_checkout(context, msg):
    state = context.state('order').unpack(Order)
    if not state:
        response = ResponseMessage()
        response.result = json.dumps({'result': 'failure',
                                      'message': 'Order does not exist.'})
        return response

    if state.paid:
        response = ResponseMessage()
        response.result = json.dumps({'result': 'failure',
                                      'message': 'Order already paid.'})

        return response

    request = Order()
    request.id = msg.order_checkout.id
    request.request_info.worker_id = msg.request_info.worker_id
    request.request_info.request_id = msg.request_info.request_id
    request.user_id = state.user_id
    # to assign a repeated field we need to call extend
    request.items.extend(state.items)
    request.total_cost = state.total_cost
    request.paid = state.paid
    request.intent = Order.Intent.PAY

    #logger.debug(f'Sending order check to payments {request}')
    # send to payment service
    context.pack_and_send("payments/pay", str(request.id), request)



def order_payment_find(context, msg):
    state = context.state('order').unpack(Order)

    request = Order()
    request.id = msg.order_id
    request.request_info.worker_id = msg.request_info.worker_id
    request.request_info.request_id = msg.request_info.request_id
    request.user_id = state.user_id
    request.items.extend(state.items)
    request.total_cost = state.total_cost
    request.paid = state.paid
    request.intent = Order.Intent.STATUS

    context.pack_and_send("payments/pay", msg.order_id, request)


def order_payment_cancel(context, msg):
    state = context.state('order').unpack(Order)
    response = OrderPaymentCancelReply()

    # if it's not yet paid return failure
    if state.paid == 0:
        response.success = 0
    else:
        state.paid = 0
        response.success = 1

    context.state('order').pack(state)

    response.request_info.worker_id = msg.request_info.worker_id
    response.request_info.request_id = msg.request_info.request_id

    context.pack_and_send("payments/pay", str(msg.order_id), response)


def order_payment_confirm(context, msg):
    response = ResponseMessage()
    if msg.actually_paid:
        state = context.state('order').unpack(Order)
        state.paid = True
        context.state('order').pack(state)

        #logger.debug("Checkout succeeded.")
        response.result = json.dumps({'result': 'success', 'message': 'Checkout succeeded.'})
    else:
        #logger.debug("Payment cancelling failed.")
        response.result = json.dumps({'result': 'failure', 'message': 'Payment cancelling failed.'})

    return response


def order_add_item_reply(context, msg):
    state = context.state('order').unpack(Order)
    response = ResponseMessage()
    if msg.result == 'success':
        #logger.info("Successfully added item to order.")
        new_item = Item()
        new_item.item_id = msg.item_id
        new_item.price = msg.price
        state.items.append(new_item)
        state.total_cost += msg.price
        #logger.info(f"{state}")
        context.state('order').pack(state)
        response.result = json.dumps({'result': 'success'})
    else:
        #logger.debug("No items left in stock.")
        response.result = json.dumps({'result': 'failure', 'message': 'No items left in stock.'})
        context.state('order').pack(state)

    return response


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
