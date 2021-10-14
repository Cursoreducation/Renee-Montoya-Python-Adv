FROM python:3.8.12

WORKDIR /application

COPY ./app2/requirements.txt /application/requirements.txt

RUN pip install -r requirements.txt

COPY ./help_text.txt /help_text.txt

CMD flask run --host=0.0.0.0 --port=8081
