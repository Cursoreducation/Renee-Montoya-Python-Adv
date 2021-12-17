from app import app
from flask import render_template
from models import Plant, Employee


@app.route('/')
def main():
     plants = Plant.query.all()
     employees = Employee.query.all()

     return render_template('index.html', plants=plants, employees=employees)


@app.route('/plant/<int:id>')
def plant(id):
     plant = Plant.query.get(id)
     return render_template('plant.html', plant=plant)


@app.route('/employee/<int:id>')
def employee(id):
     employee = Employee.query.get(id)
     employee.department = Plant.query.get(employee.department_id)
     return render_template('employee.html', employee=employee)