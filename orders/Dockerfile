FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app

COPY ./orders/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./orders/orders.py /app
COPY ./protobuf/orders_pb2.py /app
COPY ./protobuf/users_pb2.py /app
COPY ./protobuf/general_pb2.py /app

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "--access-logfile", "acc", "-w 5", "orders:app"]