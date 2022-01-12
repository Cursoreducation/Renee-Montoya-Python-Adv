import flask
from flask import request, render_template
from app import app
from config import Config
import requests
import re
# import json
from flask import jsonify


@app.route('/weather')
def weather():
    cities = re.split('%20| |,|.|-', request.args.get('city'))
    items = []
    for city in cities:
        response = requests.get(
            Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
        )
        items.append(response.json())

    return jsonify(*items)


@app.route('/get-your-weather')
def yourWeather():
    return render_template('weather.html')
