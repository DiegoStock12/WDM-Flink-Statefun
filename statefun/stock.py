""" File including the functions served by the endpoint """
import typing
import logging

from endpoints.stock_pb2 import CreateItemRequest, Count

from statefun import StatefulFunctions
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

functions = StatefulFunctions()

FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger()

# Functions to deal with stock management

# Function to create stock
# Extracts the next free stock id from its state and
# Sends a creation request to that new user function
@functions.bind("stock/create")
def create_item(context, request: CreateItemRequest):
    """ Creates an item by sending a message to the user function
    - Only has one state (int) that saves the current id to be
    asigned to the next user """

    logger.info("Creating item...")

    # get the current id to assign
    state = context.state('count').unpack(Count)
    if not state:
        logger.info("First item ever!")
        state = Count()
        state.num = 0

    # send a message to the user function to define the user
    request = CreateItemWithId()
    request.id = state.num
    print(f"Sending request to function with id {request.id}", flush=True)
    context.pack_and_send("stock/stock", str(request.id), request)

    # update the next id to assign and save
    state.num += 1
    context.state('count').pack(state)
    logger.info('Next state to assign is {}'.format(state.num))
