FROM python:latest

WORKDIR /flaskapp

COPY . /flaskapp

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
