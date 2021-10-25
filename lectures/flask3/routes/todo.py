from app import app
from flask import render_template


@app.route('/todos')
def todos_list():
    return render_template('todo.html')


@app.route('/add-todo')
def add_todo():
    return render_template('add-todo.html')