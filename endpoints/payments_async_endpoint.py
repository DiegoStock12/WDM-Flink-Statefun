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

# This endpoint will never be used, the orders function calls directly
@routes_payments.post('/payment/pay/{user_id}/{order_id}')
async def order_pay(request):
    user_id = int(request.match_info['user_id'])
    order_id = int(request.match_info['order_id'])

    msg = PaymentRequest()
    msg.user_id = user_id
    msg.order_id = order_id
    msg.request_type = PaymentRequest.RequestType.PAY
    msg.request_info.request_id = str(uuid.uuid4())
    msg.request_info.worker_id = 1 #TODO: FIXME

    result = await send_msg(PAYMENT_TOPIC, key='payment_pay', request=msg)

    r_json = json.loads(result)
    raise web.HTTPOk() if r_json['result'] == 'success' else web.HTTPNotFound()

@routes_payments.post('/payment/cancel/{user_id}/{order_id}')
async def order_cancel(request):
    user_id = int(request.match_info['user_id'])
    order_id = int(request.match_info['order_id'])

    msg = PaymentRequest()
    msg.user_id = user_id
    msg.order_id = order_id
    msg.request_type = PaymentRequest.RequestType.CANCEL
    msg.request_info.request_id = str(uuid.uuid4())
    msg.request_info.worker_id = 1 #TODO: FIXME

    result = await send_msg(PAYMENT_TOPIC, key='payment_pay', request=msg)

    r_json = json.loads(result)
    raise web.HTTPOk() if r_json['result'] == 'success' else web.HTTPNotFound()

@routes_payments.get('/payment/status/{order_id}')
async def order_status(request):
    order_id = int(request.match_info['order_id'])

    msg = PaymentRequest()
    msg.order_id = order_id
    msg.request_type = PaymentRequest.RequestType.STATUS
    msg.request_info.request_id = str(uuid.uuid4())
    msg.request_info.worker_id = 1 #TODO: FIXME

    result = await send_msg(PAYMENT_TOPIC, key='payment_pay', request=msg)

    r_json = json.loads(result)
    raise web.HTTPOk() if r_json['result'] == 'success' else web.HTTPNotFound()
