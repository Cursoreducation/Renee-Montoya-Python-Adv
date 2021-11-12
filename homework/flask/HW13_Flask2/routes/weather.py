from flask import request, render_template
from app import app
from config import Config
import requests


def get_weather(city):
    response = requests.get(
        Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
    )

    return response.json()


@app.route('/weather')
def weather():
    city = request.args.get('city')
    return get_weather(city)

#/weathers?city=Kiev,Lviv
@app.route('/weathers')
def weathers():
    cites = request.args.get('city').split(',')
    return {city: get_weather(city) for city in cites}


@app.route('/get-your-weather')
def yourWeather():
    return render_template('weather.html')
