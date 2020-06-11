FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app

COPY ./orders/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./orders/orders.py /app
COPY ./protobuf/*_pb2.py /app/

EXPOSE 8001

CMD ["gunicorn", "-b", "0.0.0.0:8001", "--access-logfile", "acc", "-w 4", "orders:app"]