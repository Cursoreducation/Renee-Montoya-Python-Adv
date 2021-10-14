from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/hello', methods=["GET", "POST"])
def index():
    return "Hello World!"

app.run(host='0.0.0.0', port=8081, debug=True)