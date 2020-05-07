""" File including the functions served by the endpoint """

from orders_pb2 import Order, CreateOrder

from statefun import StatefulFunctions
from statefun import RequestReplyHandler

functions = StatefulFunctions()


@functions.bind("orders/create")
def create_order(context, msg: CreateOrder):
    print(f"Got a message: replying...", flush=True)
    # TODO Check if user exists.
    state1 = context.state('order').unpack(Order)
    if not state1:
        print("State didn't existed", flush=True)
    else:
        print("State existed", flush=True)

    state = Order()
    state.userId = msg.userId
    state.items = [1]
    state.id = 1
    context.state('order').pack(state)


# Use the handler and expose the endpoint
handler = RequestReplyHandler(functions)

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/statefun', methods=['POST'])
def handle():
    response_data = handler(request.data)
    response = make_response(response_data)
    response.headers.set('Content-Type', 'application/octet-stream')
    return response


@app.route('/')
def welcome():
    print("asdasdasd", flush=True)
    return "This is Orders microservice!"


if __name__ == "__main__":
    app.run()


