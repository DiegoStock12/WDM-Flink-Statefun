import json
# create the logger and configure
import logging
import uuid

from aiohttp import web

from async_endpoint import send_msg
from orders_pb2 import CreateOrder, OrderRequest

# define the routes object
routes_orders = web.RouteTableDef()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"
ORDER_TOPIC = "orders"
ORDER_CREATION_TOPIC = "orders-create"
ORDER_EVENTS_TOPIC = "orders-events"


@routes_orders.get('/orders/hello')
async def add_credit(request):
    raise web.HTTPOk()


@routes_orders.post('/orders/create/{userId}')
async def create_order(request):

    userId = request.match_info['userId']
    order_id = str(uuid.uuid4())

    request = CreateOrder()
    request.user_id = userId
    request.id = order_id

    result = await send_msg(ORDER_CREATION_TOPIC, key=order_id, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.Response(text=result, status=200, content_type='application/json')
    else:
        return web.HTTPNotFound()


@routes_orders.delete('/orders/remove/{orderId}')
async def remove_order(request):

    orderId = request.match_info['orderId']
    request = OrderRequest()
    request.remove_order.id = orderId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.HTTPOk()
    else:
        return web.HTTPNotFound()


@routes_orders.get('/orders/find/{orderId}')
async def get_order(request):
    # print("Received request to find an order.", flush=True)

    orderId = request.match_info['orderId']
    request = OrderRequest()
    request.find_order.id = orderId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    r_json = json.loads(result)

    if 'result' in r_json:
        return web.HTTPNotFound()
    else:
        return web.Response(text=result, content_type='application/json')


@routes_orders.post('/orders/addItem/{orderId}/{itemId}')
async def add_item_to_order(request):
    # print("Received request to add item to an order.", flush=True)

    orderId = request.match_info['orderId']
    itemId = request.match_info['itemId']
    request = OrderRequest()
    request.add_item.id = orderId
    request.add_item.itemId = itemId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.Response(text=result, status=200, content_type='application/json')
    else:
        return web.HTTPNotFound()


@routes_orders.delete('/orders/removeItem/{orderId}/{itemId}')
async def remove_item_from_order(request):
    # print("Received request to remove item from an order.", flush=True)

    orderId = request.match_info['orderId']
    itemId = request.match_info['itemId']
    request = OrderRequest()
    request.remove_item.id = orderId
    request.remove_item.itemId = itemId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.Response(text=result, content_type='application/json')
    else:
        return web.HTTPNotFound()


@routes_orders.post('/orders/checkout/{orderId}')
async def checkout_order(request):
    # print("Received request to checkout the order.", flush=True)

    orderId = request.match_info['orderId']
    request = OrderRequest()
    request.order_checkout.id = orderId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.Response(text=result, content_type='application/json')
    else:
        return web.HTTPNotFound()