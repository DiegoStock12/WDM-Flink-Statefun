from aiohttp import web
import asyncio

from async_endpoint import app, send_msg, messages, WORKER_ID

# create the logger and configure
import logging
import json
# define the routes object
from payment_pb2 import PaymentRequest

routes_payments = web.RouteTableDef()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"
PAYMENT_INPUT_TOPIC = "payments"


@routes_payments.post('/payment/cancel/{user_id}/{order_id}')
async def payment_cancel(request):
    user_id = request.match_info['user_id']
    order_id = request.match_info['order_id']

    msg = PaymentRequest()
    msg.user_id = user_id
    msg.order_id = order_id
    msg.request_type = PaymentRequest.RequestType.CANCEL

    result = await send_msg(PAYMENT_INPUT_TOPIC, key=order_id, request=msg)

    r_json = json.loads(result)
    raise web.HTTPOk() if r_json['result'] == 'success' else web.HTTPNotFound()


@routes_payments.get('/payment/status/{order_id}')
async def payment_status(request):
    order_id = request.match_info['order_id']

    msg = PaymentRequest()
    msg.order_id = order_id
    msg.request_type = PaymentRequest.RequestType.STATUS

    #logger.info('Payments sending message')

    result = await send_msg(PAYMENT_INPUT_TOPIC, key=order_id, request=msg)

    r_json = json.loads(result)

    return web.Response(text=json.dumps(r_json), content_type='application/json')
