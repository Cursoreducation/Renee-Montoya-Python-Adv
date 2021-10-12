from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://app1:8080/')
    print(response.content)
    return response.json()[1]['first_name']

app.run(host='0.0.0.0', port=8081, debug=True)