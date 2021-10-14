from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:flask@mysql/flask'
db = SQLAlchemy(app)


@app.route('/')
def index():
    data = json.dumps([{"first_name": "Libomyr"}, {"first_name": "Ivan"}])
    return data

app.run(host='0.0.0.0', port=8080, debug=True)