""" File including the functions served by the endpoint """
import typing

from example_pb2 import IncreaseUserCount, User, ExampleRequest, ExampleResponse

from statefun import StatefulFunctions
from statefun import RequestReplyHandler

functions = StatefulFunctions()

@functions.bind("example/increment")
def increment_user(context, request: IncreaseUserCount):
    state = context.state('user').unpack(User)
    if not state:
        print(f"First time I see this user {request.name}", flush=True)
        state = User()
        state.count = 1
    else:
        state.count += 1
    context.state('user').pack(state)

    print(f"Current number for user {request.name} is {state.count}", flush=True)

@functions.bind("example/request")
def send_request(context, msg : typing.Union[ExampleRequest, ExampleResponse]):
    if isinstance(msg, ExampleRequest):
        print("Got a new request!, Sending message to other function", flush=True)
        m = ExampleRequest()
        m.message = msg.message
        context.pack_and_send("example/reply", "id", m)
    
    elif isinstance(msg, ExampleResponse):
        print(f"Got an example response with message {msg.message}", flush =True)

@functions.bind("example/reply")
def send_reponse(context, msg: ExampleRequest):
    print(f"Got a message: {msg.message} replying...", flush =True)
    m = ExampleResponse()
    m.message = "repliying to you from example/reply"
    context.pack_and_reply(m)


# Use the handler and expose the endpoint
handler = RequestReplyHandler(functions)

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/statefun', methods=['POST'])
def handle():
    response_data = handler(request.data)
    response = make_response(response_data)
    response.headers.set('Content-Type', 'application/octet-stream')
    return response

@app.route('/')
def welcome():
    return "Hello world!"


if __name__ == "__main__":
    app.run()


