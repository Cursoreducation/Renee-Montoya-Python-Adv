from flask import Flask, render_template, request, redirect

app = Flask(__name__)

text_global = []


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


def calc(first_argument, second_argument, operation):
    if first_argument is None or first_argument == '':
        first_argument = 0
    try:
        first_argument = int(first_argument)
    except ValueError:
        return 'First argument is Incorrect'
    try:
        first_argument = int(second_argument)
    except ValueError:
        return 'Second argument is Incorrect'
    if operation == '+':
        result = first_argument + second_argument
    elif operation == '*':
        result = first_argument * second_argument
    elif operation == '/':
        if second_argument == 0:
            return 'Division by zero'
        result = first_argument / second_argument
    elif operation == '-':
        result = first_argument - second_argument
    else:
        result = 'unknown operation'
    return result


@app.route('/calc/<int:first_num>/<int:second_num>/<operator>', methods=["GET"])
def calc_endpoint(first_num, second_num, operator):
    if operator == 'div':
        operator = '/'
    elif operator == 'sum':
        operator = '+'
    elif operator == 'dif':
        operator = '-'
    elif operator == 'mult':
        operator = '*'
    result = calc(first_num, second_num, operator)
    return render_template('result.html',
                           first_arg=first_num,
                           second_arg=second_num,
                           operation=operator,
                           result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
