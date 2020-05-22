from aiohttp import web
import asyncio

from async_endpoint import app, send_msg, messages, WORKER_ID
from users_pb2 import CreateUserRequest, UserRequest, UserResponse

# create the logger and configure
import logging
import json
# define the routes object
routes_users = web.RouteTableDef()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

# Some parameters to send and read from kafka
KAFKA_BROKER = "kafka-broker:9092"
USER_TOPIC = "users"
USER_CREATION_TOPIC = "users-create"
USER_EVENTS_TOPIC = "user-events"

# Declaration of the user endpoints
@routes_users.post('/users/create')
async def create_user(request):
    """ Sends a create user request to the cluster"""
    msg = CreateUserRequest()

    # wait for the response asynchronously
    result = await send_msg(USER_CREATION_TOPIC, key="create", request=msg)

    return web.Response(text=result, content_type='application/json')


@routes_users.delete('/users/remove/{user_id}')
async def remove_user(request):
    """ Sends a remove user request to the statefun cluster"""

    user_id = int(request.match_info['user_id'])

    msg = UserRequest()
    msg.remove_user.id = user_id

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    # return code 200 or 404 in case of success or failure
    r_json = json.loads(result)
    raise web.HTTPOk() if r_json['result'] == 'success' else web.HTTPNotFound()


@routes_users.get('/users/find/{user_id}')
async def find_user(request):

    user_id = int(request.match_info['user_id'])

    msg = UserRequest()
    msg.find_user.id = user_id

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    return web.Response(text=result, content_type='application/json')


@routes_users.get('/users/credit/{user_id}')
async def get_credit(request):
    # this can do the same as the find user as long as
    # we just return the number only

    # we get the result that is a dict of {'id': 0,
    #                                       ' credit': 100}
    # and we need to extract the credit from there and return it
    response: web.Response = await find_user(request)

    r_json = json.loads(response.text)

    return web.Response(
        text=json.dumps({'credit': r_json['credit']}),
        content_type='application/json'
    )


@routes_users.post('/users/credit/subtract/{user_id}/{amount}')
async def subtract_credit(request):

    user_id = int(request.match_info['user_id'])
    amount = int(request.match_info['amount'])

    msg = UserRequest()
    msg.subtract_credit.id = user_id
    msg.subtract_credit.amount = amount

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    # return code 200 or 404 in case of success or failure
    r_json = json.loads(result)
    raise web.HTTPOk(
    ) if r_json['result'] == 'success' else web.HTTPBadRequest()


@routes_users.post('/users/credit/add/{user_id}/{amount}')
async def add_credit(request):

    user_id = int(request.match_info['user_id'])
    amount = int(request.match_info['amount'])

    msg = UserRequest()
    msg.add_credit.id = user_id
    msg.add_credit.amount = amount

    result = await send_msg(USER_TOPIC, key=user_id, request=msg)

    # return code 200 or 404 in case of success or failure
    r_json = json.loads(result)
    raise web.HTTPOk(
    ) if r_json['result'] == 'success' else web.HTTPBadRequest()