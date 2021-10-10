FROM ubuntu:latest

WORKDIR /flaskapp

RUN apt-get update && apt-get install -y python3-pip python3

COPY . /flaskapp
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
