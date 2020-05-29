FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app


COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY payments.py /app
COPY users_pb2.py /app
COPY general_pb2.py /app
COPY payment_pb2.py /app
COPY orders_pb2.py /app

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w 4", "payments:app"]