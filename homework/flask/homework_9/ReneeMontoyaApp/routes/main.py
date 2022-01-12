from app import app, db
from flask import render_template, request, redirect, url_for, flash
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


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
    plant = Plant.query.get(id)
    form_data = request.form
    plant.name = form_data.get('name')
    plant.location = form_data.get('location')
    plant.director_id = form_data.get('director_id')
    db.session.add(plant)
    db.session.commit()
    return redirect(url_for('plant', id=id))


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    return render_template('employee.html', employee=employee)


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id, error=None):
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('edit-employee.html', plants=plants, employee=employee, salons=salons, error=error)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
    error = None
    employee = Employee.query.get(id)
    form_data = request.form
    employee.email = form_data.get('email') if form_data.get('email') != None else employee.email
    employee.name = form_data.get('name') if form_data.get('name') != None else employee.email
    employee.department_type = form_data.get('department_type')
    employee.department_id = form_data.get('department_id')
    if form_data.get('department_id') == None\
            or form_data.get('department_type') == None:
        error = 'Invalid department'
        return redirect(url_for('employee_edit_page', id=id, error=error))
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    return render_template('salon.html', salon=salon)
