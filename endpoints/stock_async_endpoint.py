from aiohttp import web
from async_endpoint import send_msg
from stock_pb2 import *

# create the logger and configure
import logging
import uuid

# define the routes object
routes_stock = web.RouteTableDef()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"
STOCK_TOPIC = "stock"
STOCK_CREATION_TOPIC = "stock-create"
STOCK_EVENTS_TOPIC = "stock-events"


@routes_stock.post('/stock/item/create/{price}')
async def stock_create_item(request):
    price = int(request.match_info['price'])

    item_id = str(uuid.uuid4())

    msg = CreateItemRequest()
    msg.price = price
    msg.id = item_id


    result = await send_msg(STOCK_CREATION_TOPIC, key=item_id, request=msg)
    return web.Response(text=result, content_type='application/json')


@routes_stock.get('/stock/find/{item_id}')
async def stock_find_item(request):
    item_id = request.match_info['item_id']

    msg = StockRequest()
    msg.find_item.id = item_id

    result = await send_msg(STOCK_TOPIC, key=item_id, request=msg)

    if "not_found" in result:
        return web.Response(text=result, status=404, content_type='application/json')

    return web.Response(text=result, content_type='application/json')


@routes_stock.post('/stock/add/{item_id}/{number}')
async def item_add_stock(request):
    item_id = request.match_info['item_id']
    number = int(request.match_info['number'])

    msg = StockRequest()
    msg.add_stock.id = item_id
    msg.add_stock.amount = number

    result = await send_msg(STOCK_TOPIC, key=item_id, request=msg)

    if "not_found" in result:
        return web.Response(text=result, status=404, content_type='application/json')

    return web.Response(text=result, content_type='application/json')


@routes_stock.post('/stock/subtract/{item_id}/{number}')
async def item_substract_stock(request):
    item_id = request.match_info['item_id']
    number = int(request.match_info['number'])

    msg = StockRequest()
    msg.subtract_stock.id = item_id
    msg.subtract_stock.amount = number

    result = await send_msg(STOCK_TOPIC, key=item_id, request=msg)

    if "not_found" in result:
        return web.Response(text=result, status=404, content_type='application/json')

    if "stock too low" in result:
        return web.Response(text=result, status=400, content_type='application/json')

    return web.Response(text=result, content_type='application/json')
