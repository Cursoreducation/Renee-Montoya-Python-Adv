from flask import Flask
from flask_restful import Api
from config import Config

app = Flask(__name__)
api = Api(app)

print(Config.WEATHER_API_KEY)
print(Config.WEATHER_API_URL)

with app.app_context():
    from routes.lecture1 import *
    from routes.weather import *
    from routes.todo import *
    from routes.api.todo import *

app.run(debug=True)