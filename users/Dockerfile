FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app



COPY ./users/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./users/users.py /app
COPY ./protobuf/users_pb2.py /app
COPY ./protobuf/general_pb2.py /app

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "-w 4", "users:app"]