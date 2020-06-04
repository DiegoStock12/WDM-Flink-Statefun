from aiohttp import web
import asyncio

from async_endpoint import app, send_msg, messages, WORKER_ID
from orders_pb2 import CreateOrder, OrderRequest

# create the logger and configure
import logging
import json

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
    print("Received request to create order for user", flush=True)

    userId = int(request.match_info['userId'])
    if (userId < 0):
        return web.HTTPNotFound()

    request = CreateOrder()
    request.user_id = userId

    result = await send_msg(ORDER_CREATION_TOPIC, key=userId, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.Response(text=result, status=200, content_type='application/json')
    else:
        return web.HTTPNotFound()


@routes_orders.delete('/orders/remove/{orderId}')
async def remove_order(request):
    print("Received request to remove order.", flush=True)

    orderId = int(request.match_info['orderId'])
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
    print("Received request to find an order.", flush=True)

    orderId = int(request.match_info['orderId'])
    request = OrderRequest()
    request.find_order.id = orderId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    print(f'Result: {result}', flush=True)
    r_json = json.loads(result)

    if 'result' in r_json:
        return web.HTTPNotFound()
    else:
        return web.Response(text=result, content_type='application/json')


@routes_orders.post('/orders/addItem/{orderId}/{itemId}')
async def add_item_to_order(request):
    print("Received request to add item to an order.", flush=True)

    orderId = int(request.match_info['orderId'])
    itemId = int(request.match_info['itemId'])
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
    print("Received request to remove item from an order.", flush=True)

    orderId = int(request.match_info['orderId'])
    itemId = int(request.match_info['itemId'])
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
    print("Received request to checkout the order.", flush=True)

    orderId = int(request.match_info['orderId'])
    request = OrderRequest()
    request.order_checkout.id = orderId

    result = await send_msg(ORDER_TOPIC, key=orderId, request=request)
    r_json = json.loads(result)

    if r_json['result'] == 'success':
        return web.Response(text=result, content_type='application/json')
    else:
        return web.HTTPNotFound()