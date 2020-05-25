FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app


COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY stock.py /app
COPY stock_pb2.py /app
COPY general_pb2.py /app

EXPOSE 8002

CMD ["gunicorn", "-b", "0.0.0.0:8002", "-w 4", "stock:app"]