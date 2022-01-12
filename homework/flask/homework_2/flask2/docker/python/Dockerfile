FROM python:3.8.12

ENV PYTHONUNBUFFERED 1

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=8080
