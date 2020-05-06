""" File including the functions served by the endpoint """

from example_pb2 import IncreaseUserCount, User

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


