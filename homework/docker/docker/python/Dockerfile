FROM ubuntu:latest

WORKDIR /application

RUN apt-get update && apt-get install -y python3 python3-pip

CMD pip install -r requirements.txt

CMD python3 app.py
