from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
@app.route('/calc', methods=["GET"])
def index():
    argument = [5.0, 2.0]
    return render_template('index.html', arg1=argument[0], arg2=argument[1])


@app.route('/calc/5/2/sum', methods=["POST"])
def addition():
    form = request.form
    argument = []
    argument.append(float(form['arg1']))
    argument.append(float(form['arg2']))
    return render_template('result.html', op="+", arg1=argument[0],
                           arg2=argument[1], result=argument[0] + argument[1])


@app.route('/calc/5/2/dif', methods=["POST"])
def subtraction():
    form = request.form
    argument = []
    argument.append(float(form['arg1']))
    argument.append(float(form['arg2']))
    return render_template('result.html',  op="-", arg1=argument[0],
                           arg2=argument[1], result=argument[0] - argument[1])


@app.route('/calc/5/2/mult', methods=["POST"])
def multiplication():
    form = request.form
    argument = []
    argument.append(float(form['arg1']))
    argument.append(float(form['arg2']))
    return render_template('result.html',  op="*", arg1=argument[0],
                           arg2=argument[1], result=argument[0] * argument[1])


@app.route('/calc/5/2/div', methods=["POST"])
def division():
    form = request.form
    argument = []
    argument.append(float(form['arg1']))
    argument.append(float(form['arg2']))
    return render_template('result.html',  op="/", arg1=argument[0],
                           arg2=argument[1], result=argument[0] / argument[1])


app.run(host='0.0.0.0', port=8080, debug=True)
