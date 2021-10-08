FROM ubuntu:latest

WORKDIR /application

RUN apt-get update && apt-get install -y python3-pip python3

COPY ./help_text.txt /help_text.txt

CMD python3 app.py
