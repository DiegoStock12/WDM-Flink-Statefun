FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app


COPY ./stock/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./stock/stock.py /app
COPY ./protobuf/stock_pb2.py /app
COPY ./protobuf/general_pb2.py /app

EXPOSE 8002

CMD ["gunicorn", "-b", "0.0.0.0:8002", "-w 4", "stock:app"]