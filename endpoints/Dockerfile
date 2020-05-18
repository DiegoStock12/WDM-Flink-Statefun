FROM python:3.7-slim-buster
# had to change the image so aiohttp could
# build (needed dcc and some basic libraries that
# the alpine version didn't have)

RUN mkdir -p /app
WORKDIR /app

# RUN apk add gcc

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY users.py /app
COPY async_endpoint.py /app
COPY users_async_endpoint.py /app
COPY orders_async_endpoint.py /app
COPY users_pb2.py /app
COPY orders_pb2.py /app
COPY general_pb2.py /app
COPY stock_pb2.py /app
COPY stock_async_endpoint.py /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "acc", "-w 4", "--worker-class", "aiohttp.GunicornWebWorker", "async_endpoint:app"]
