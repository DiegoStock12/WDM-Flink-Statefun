
from stock_pb2 import *

@routes.post('/stock/item/create/{price}')
async def stock_create_item(request):
    price = int(request.match_info['price'])

    msg = CreateItemRequest()
    msg.price = price

    result = await send_msg(STOCK_CREATION_TOPIC, key="create", request=msg)
    return web.Response(text=result, content_type='application/json')