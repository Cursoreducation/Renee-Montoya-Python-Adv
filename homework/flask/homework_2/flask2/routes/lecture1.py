from flask import render_template, request, redirect
from app import app
from config import Config


text_global = []


@app.route('/', methods=["GET"])
def index():
    return Config.WEATHER_API_KEY


@app.route('/display-text', methods=["GET"])
def text():
    global text_global
    return render_template('text.html', text=text_global)


@app.route('/text/new/', methods=["GET"])
def text_new():
    return render_template('text_form.html')


@app.route('/save', methods=["POST"])
def save():
    global text_global
    form = request.form
    text_global = form['text']
    return redirect('/display-text')
