# WDM-Flink-Statefun
Instructions for getting the Apache Flink Docker container:
* `git clone https://github.com/apache/flink-statefun-docker`
* `cd 2.0.0`
* `docker build -t flink-statefun:2.0.0 .`

Run the whole demo:
* `docker-compose up`

Rebuild single container:
* `docker-compose up -d --no-deps --build <service-name>`

Rebuild everying after you changed files (do this before docker-compose up, otherwise it will stil run old containers):
* `docker-compose build`

Compile proto files example:
* `protoc --proto_path=payments/protobuf/ --python_out=payments/ payments/protobuf/orders.proto`


## User Service

Takes care of user IDs and the credit they have, as well as adding, removing users or increasing or decreasing the credit. The functionality as with other services is divided between the user endpoint and the user stateful functions.

### User Endpoint

Takes requests from users and communicates with Flink and the state by means of sending and receiving Kafka messages. The following endpoints are available

- `/users/create` (POST): Creates a user and returns its assigned ID
- `/users/find/<id>` (GET): Retrieves the user's id and credit
- `/users/remove/<id>` (DELETE): Removes that user's data from the system and returns  either `success`  or `failure`
- `/users/credit/<id>` (GET): Retrieves the given user's credit
- `/users/credit/add/<id>/<amount>` (POST): Adds a certain amount of credit to the account of a specific user, returns either `success`  or `failure`
- `/users/credit/subtract/<id>/<amount>` (POST): Decrements that user's credit by the specified amount, return either `success`  or `failure`

All those endpoints send their requests either to the `users` topic or the `users-create` topic, which triggers one of the corresponding stateful functions.

### Stateful Functions

The stateful functions preserve the state of each user and receive events from the endpoint via kafka messages. We have one virtual actor or function per user, as well as a lone function for creating users that keeps track of the next available id to assign. The functions are:

- `users/create`: Assigns an user the next free id and calls the main user function to initialize the credit
- `users/user`: Main function of each user which holds its state. The state has two components: id and credit. Depending on the message received by the function, different actions are performed according to those defined in the endpoint.

After processing the requests, the result of the computation is published in the `user-events` topic within a general `UserResponse` protobuf message. The actual response that will be displayed to the caller is embedded in the `result` field of that protobuf in JSON format.

# Resources
- [Stateful functions - keynote](https://www.youtube.com/watch?v=NF0hXZfUyqE&feature=youtu.be)
- [Stateful functions - demo](https://www.youtube.com/watch?v=tuSylBadNSo)
- [Kafka client - benchmarks](https://activisiongamescience.github.io/2016/06/15/Kafka-Client-Benchmarking/)
- [Python WSGI servers - performance analysis](https://www.appdynamics.com/blog/engineering/a-performance-analysis-of-python-wsgi-servers-part-2/)

# Ask Asterios

* How do we scale the Flink side -> not just duplicating containers, need to share state as well -> how to configure and define this in Kubernetes?
* What about the replies -> should be non-blocking -> save ID per request and listen on an reply output topic?
* Is return success/failure JSON or simply a status code?
* Should the ID also be in a JSON field?
* /orders/find/{order_id} -> what if an order does not exist?
