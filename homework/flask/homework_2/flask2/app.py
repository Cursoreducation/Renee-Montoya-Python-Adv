from flask import Flask
from config import Config

app = Flask(__name__)

print(Config.WEATHER_API_KEY)
print(Config.WEATHER_API_URL)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

with app.app_context():
    from routes.lecture1 import *
    from routes.weather import *

app.run(debug=True)