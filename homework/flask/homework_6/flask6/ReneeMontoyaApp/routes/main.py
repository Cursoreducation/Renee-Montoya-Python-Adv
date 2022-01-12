from app import app
from flask import render_template
from models import Plant, Employee, Salon


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()
    return render_template('index.html', plants=plants, employees=employees, salons=salons)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    return render_template('plant.html', plant=plant)


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    employee.department = Plant.query.get(employee.department_id)
    return render_template('employee.html', employee=employee)


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    salon.director = Salon.query.get(salon.director_id)
    return render_template('salon.html', salon=salon)
