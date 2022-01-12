from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


with app.app_context():
    from routes.todo import *
    from routes.api.todo import *

app.run(debug=True)
