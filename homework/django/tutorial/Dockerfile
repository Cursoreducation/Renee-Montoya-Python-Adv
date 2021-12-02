FROM python:3.9.7-buster

WORKDIR /application
COPY requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt
COPY ./tutorial /application

CMD python3 manage.py runserver 0.0.0.0:8000
