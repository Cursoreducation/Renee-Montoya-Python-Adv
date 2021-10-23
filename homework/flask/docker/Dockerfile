FROM python:3.9.7-buster

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=9090
