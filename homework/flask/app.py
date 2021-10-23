from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')
    
def calculator(val_one, val_two, action):
    try:
        val_one = int(val_one)
    except ValueError:
        return 'val_one is bad'
    try:
        val_two = int(val_two)
    except ValueError:
        return 'val_two is bad'
    if action == '/':
        result = val_one / val_two
    elif action == '+':
        result = val_one + val_two
    elif action == '-':
        result = val_one - val_two
    elif action == '*':
        result = val_one * val_two
    else:
    	result = 'nothing'
    return result
    
@app.route('/calc/<int:value_one>/<int:value_two>/<oper>', methods=["GET", "POST"])
def act(value_one, value_two, oper):
    actions = ['/', '+', '-', '*']
    if oper == 'div':
        oper = '/'
    elif oper == 'sum':
        oper = '+'
    elif oper == 'dif':
        oper = '-'
    elif oper == 'mul':
        oper = '*'
    result = calculator(value_one, value_two, oper)
    return render_template('result.html', num_one=value_one, num_two=value_two, action=oper, result=result)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
