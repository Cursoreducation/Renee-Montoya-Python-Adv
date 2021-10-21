FROM python:latest

WORKDIR /flask

COPY ./requirements.txt /flask/requirements.txt

RUN pip install -r requirements.txt
RUN pip install -U pip

CMD python3 app.py
