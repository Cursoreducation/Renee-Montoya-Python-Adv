FROM python:3.9.7-buster

WORKDIR /flaskapp

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
