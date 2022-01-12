from flask import Flask, render_template
from result import Result

# create app
app = Flask(__name__)


@app.route('/', methods=["GET"])
def home_page():
    return render_template('index.html')


@app.route('/calc/<int:numb1>/<int:numb2>/<string:op>', methods=["GET"])
def calculate(numb1, numb2, op):
    if op == 'div':
        calc_res = Result(numb1, numb2).div_res()
    elif op == 'sum':
        calc_res = Result(numb1, numb2).sum_res()
    elif op == 'dif':
        calc_res = Result(numb1, numb2).dif_res()
    elif op == 'mult':
        calc_res = Result(numb1, numb2).mult_res()
    else:
        calc_res = 'Wrong operation'
    print(calc_res)
    return render_template('result.html', calc=calc_res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
