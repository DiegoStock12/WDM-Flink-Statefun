from aiohttp import web
import asyncio

from async_endpoint import app, send_msg, messages, WORKER_ID
from users_pb2 import CreateUserRequest, UserRequest, UserResponse

# create the logger and configure
import logging
import json
# define the routes object
routes_payments = web.RouteTableDef()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"
PAYMENT_TOPIC = "payment-create"

@routes_payments.post('/payment/pay/{user_id}/{order_id}')
async def order_pay(request):

    user_id = int(request.match_info['user_id'])
    order_id = int(request.match_info['order_id'])

    msg = PaymentRequest()
    msg.user_id = user_id
    msg.order_id = order_id
    msg.request_type = PaymentRequest.RequestType.PAY
    msg.request_id = str(uuid.uuid4())

    send_msg(PAYMENT_TOPIC, key='payment_pay', request=msg)

    result = get_message(msg.request_id)

    return result

# todo: fixme
@routes_payments.post('/payment/cancel/{user_id}/{order_id}')
def order_cancel(user_id, order_id):
    request = PaymentRequest()
    request.user_id = user_id
    request.order_id = order_id
    request.request_type = PaymentRequest.RequestType.CANCEL
    request.request_id = str(uuid.uuid4())

    send_msg(PAYMENT_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return result

# todo: fixme
@routes_payments.get('/payment/status/{order_id}', methods=['GET'])
def order_status(order_id):
    request = PaymentRequest()
    request.order_id = order_id
    request.request_type = PaymentRequest.RequestType.STATUS
    requests.request_id = str(uuid.uuid4())

    send_msg(PAYMENT_TOPIC, key=user_id, request=request)

    result = get_message(request.request_id)

    return result
