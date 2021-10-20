from flask import Flask, render_template, request, redirect

app = Flask(__name__)

text_global = []

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

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


app.run(host='0.0.0.0', port=8080, debug=True)