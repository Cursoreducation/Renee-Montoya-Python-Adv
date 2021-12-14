FROM python:3.8.12

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt

#CMD wait-for-it.sh db:3306 -t 10 -- python3 app.py
CMD python3 app.py
