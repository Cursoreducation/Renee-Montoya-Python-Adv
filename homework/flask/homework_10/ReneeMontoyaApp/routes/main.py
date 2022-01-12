from app import app, db
from flask import render_template, request, redirect, url_for, session
from utils.helpers import encrypt_string
from models import Plant, Employee, Salon


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()
    return render_template('index.html', plants=plants, employees=employees, salons=salons, session=session)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    return render_template('plant.html', plant=plant, session=session)


@app.route('/login')
def login():
     return render_template('login.html', session=session)


@app.route('/auth', methods=['POST'])
def auth():
    form = request.form
    user = Employee.query.filter(Employee.email == form['login']).filter(Employee.password == encrypt_string(form['password'])).first()
    if user is None:
        error = "Invalid email or password"
        return render_template('login.html', session=session, error=error)
    session['user'] = user.serialize
    return redirect('http://localhost:8082/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('http://localhost:8080/')


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    plant = Plant.query.get(id)
    if session.get('user') is None:
        error = "Only authorized users can edit"
        return render_template('plant.html', plant=plant, session=session, error=error)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees, session=session)


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
    return render_template('employee.html', employee=employee, session=session)


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id, error=None):
    employee = Employee.query.get(id)
    if session.get('user') is None:
        error = "Only authorized users can edit"
        return render_template('employee.html', employee=employee, error=error, ession=session)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('edit-employee.html', plants=plants, employee=employee, salons=salons, error=error, session=session)


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
        return redirect(url_for('employee_edit_page', id=id, error=error, session=session))
    if session.get('user') is None:
        error = "Only authorized users can edit"
        return render_template('employee.html', employee=employee, error=error, session=session)
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    return render_template('salon.html', salon=salon, session=session)

