from app import app
from flask import render_template

@app.route('/')
def main():
    return "Hello World!"

@app.route('/error')
def gen_error():
    return int("Hello World!")


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500