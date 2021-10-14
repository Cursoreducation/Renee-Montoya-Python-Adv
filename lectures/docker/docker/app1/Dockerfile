FROM python:3.10.0-slim-buster

WORKDIR /application

COPY ./app1/requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt

COPY ./help_text.txt /help_text.txt

CMD flask run --host=0.0.0.0 --port=8080
