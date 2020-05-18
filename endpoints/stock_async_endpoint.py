from aiohttp import web
import asyncio

from async_endpoint import app, send_msg, messages, WORKER_ID
from stock_pb2 import *

# create the logger and configure
import logging

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

    msg = CreateItemRequest()
    msg.price = price

    result = await send_msg(STOCK_CREATION_TOPIC, key="create", request=msg)
    return web.Response(text=result, content_type='application/json')