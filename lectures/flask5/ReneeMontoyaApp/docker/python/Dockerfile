FROM python:3.8.12

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt

CMD python3 app.py
