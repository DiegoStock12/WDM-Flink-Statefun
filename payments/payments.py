""" File including the functions served by the endpoint """
from flask import Flask, request, jsonify, make_response
import typing
import logging
import json

# Messages and internal states of the functions
from users_pb2 import CreateUserRequest, UserRequest, UserResponse, UserData, Count, CreateUserWithId, UserPay

from statefun import StatefulFunctions
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

PAYMENT_EVENTS_TOPIC = "payment-events"

# Logging config
FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()


# Topic to output the responses to
USER_EVENTS_TOPIC = "user-events"

# Functions where to bind
functions = StatefulFunctions()

@functions.bind('payments/pay')
def payments_pay(context, request: typing.Union[PaymentRequest, Order, OrdersPayReply, OrderPaymentCancelReply]):

    # if isinstance(request, UserRequest):


    if request.request_type == PaymentRequest.RequestType.PAY:
        # send message to orders/find -> blocking wait here? get total price back in another function?

        orders_pay_find = OrdersPayFind()
        orders_pay_find.request_info.request_id = request.request_id
        orders_pay_find.request_info.worker_id = request.worker_id
        orders_pay_find.order_id = request.order_id

        # subtract amount from user -> get success/failure back
        user_pay_request = UserPayRequest()
        user_pay_request.request_info.request_id = request.request_id
        user_pay_request.request_info.worker_id = request.worker_id
        user_pay_request.amount = 100 # todo: fixme
        context.pack_and_send("users/user", request.user_id, user_pay_request)



        # return success / failure to orders function
        pass
    elif request.request_type == PaymentRequest.RequestType.CANCEL:
        # send message to orders/find -> get total price back in another function?

        # send message to user add to add the amount of the order -> get success/failure back

        # send message to orders to mark orders as unpaid
        pass
    elif: request.request_type == PaymentRequest.RequestType.STATUS:
        # call orders/find and return status from there

        pass


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
