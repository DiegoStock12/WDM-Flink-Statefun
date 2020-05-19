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
def payments_pay(context, request: typing.Union[PaymentRequest, UserPayRequest, Order, OrdersPayFind, UserPayResponse, OrdersPayReply, OrderPaymentCancelReply]):

    if isinstance(request, Order):
        if request.intent == Order.Intent.PAY:
            user_pay_request = UserPayRequest()
            user_pay_request.request_info.request_id = request.request_info.request_id
            user_pay_request.request_info.worker_id = request.request_info.worker_id
            user_pay_request.order_id = request.order_id
            user_pay_request.amount = request.total_cost
            context.pack_and_send("users/user", request.user_id, user_pay_request)
        elif request.intent == Order.Intent.CANCEL:
            if request.paid == False:
                # Payment cannot be cancelled cause it is not paid
                payment_response = ResponseMessage()
                payment_response.result = json.dumps({'result': 'failure'})
                # TODO: is this correct?
                egress_message = kafka_egress_record(
                    topic=PAYMENT_EVENTS_TOPIC,
                    key=request.worker_id,
                    value=payment_response
                )
                context.pack_and_send_egress("payments/out", egress_message)
            # Otherwise send request to user to subtract the amount
            elif request.paid == True:
                user_pay_request = UserCancelPayRequest()
                user_pay_request.request_info.request_id = request.request_info.request_id
                user_pay_request.request_info.worker_id = request.request_info.worker_id
                user_pay_request.order_id = request.order_id
                user_pay_request.amount = request.total_cost
                context.pack_and_send("users/user", request.user_id, user_pay_request)
        elif request.intent == Order.Intent.STATUS:
            payment_response = ResponseMessage()
            payment_response.result = json.dumps({'paid': True}) if request.paid else json.dumps({'paid': False})
            # TODO: is this correct?
            egress_message = kafka_egress_record(
                topic=PAYMENT_EVENTS_TOPIC,
                key=request.worker_id,
                value=payment_response
            )
            context.pack_and_send_egress("payments/out", egress_message)
    elif isinstance(request, UserPayResponse):
        payment_status = PaymentStatus()
        payment_status.order_id = request.order_id
        payment_status.actually_paid = request.success
        payment_status.request_info.request_id = request.request_info.request_id
        payment_status.request_info.worker_id = request.request_info.worker_id
        context.pack_and_send("orders/checkout", request.user_id, payment_status)
    elif isinstance(request, PaymentRequest):
        if request.request_type == PaymentRequest.RequestType.CANCEL:
            order_payment_cancel_request = OrderPaymentCancel()
            order_payment_cancel_request.order_id = request.order_id
            order_payment_cancel_request.request_info.request_id = request.request_info.request_id
            order_payment_cancel_request.request_info.worker_id = request.request_info.worker_id
            context.pack_and_send("orders/checkout", request.user_id, order_payment_cancel_request)
        elif request.request_type == PaymentRequest.RequestType.STATUS:
            orders_pay_find_request = OrdersPayFind()
            orders_pay_find_request.order_id = request.order_id
            orders_pay_find_request.request_info.request_id = request.request_info.request_id
            orders_pay_find_request.request_info.worker_id = request.request_info.worker_id
            context.pack_and_send("orders/order", request.user_id, orders_pay_find_request)
    elif isinstance(request, OrderPaymentCancelReply):
        payment_response = ResponseMessage()
        payment_response.result = json.dumps({'result': 'success'}) if request.success else json.dumps({'result': 'failure'})
        egress_message = kafka_egress_record(
            topic=PAYMENT_EVENTS_TOPIC,
            key=request.worker_id,
            value=payment_response
        )
        context.pack_and_send_egress("payments/out", egress_message)


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
