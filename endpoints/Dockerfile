FROM python:3.7-slim-buster
# had to change the image so aiohttp could
# build (needed dcc and some basic libraries that
# the alpine version didn't have)

RUN mkdir -p /app
WORKDIR /app

# RUN apk add gcc

COPY ./endpoints/requirements.txt /app
RUN pip install -r requirements.txt

# COPY users.py /app
COPY ./endpoints/async_endpoint.py /app
COPY ./endpoints/*_async_endpoint.py /app/

COPY ./protobuf/*_pb2.py /app/

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "--access-logfile", "acc", "-w 9", "--worker-class", "aiohttp.GunicornWebWorker", "async_endpoint:app"]
