FROM python:latest

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt

RUN pip install -U pip

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=8080
