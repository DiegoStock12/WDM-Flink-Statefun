FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app


COPY ./payments/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./payments/payments.py /app
COPY ./protobuf/users_pb2.py /app
COPY ./protobuf/general_pb2.py /app
COPY ./protobuf/payment_pb2.py /app
COPY ./protobuf/orders_pb2.py /app

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "-w 5", "payments:app"]
