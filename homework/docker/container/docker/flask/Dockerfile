FROM python:3.10.0-slim-buster

WORKDIR /application

COPY requirements.txt /application/requirements.txt
COPY shop.sql /application/shop.sql

# RUN apt-get update && apt-get -y install mysql-common && apt-get -y install mycli
RUN pip install -r requirements.txt
# RUN mysql -uflask -pflash -happ flask <shop.sql


CMD flask run --host=0.0.0.0 --port=8080
