from app import app, api, db
from models import Employee
from flask import request
from flask_restful import Resource
from utils.helpers import convert_list


class EmployeeResource(Resource):
    def get(self):
        employees = Employee.query.all()
        return convert_list(employees)

    def post(self):
        request_data = request.json
        employee = Employee(
            name=request_data['name'],
            email=request_data['email'],
            department_type=request_data['department_type'],
            department_id = int(request_data['deparment_id']),
        )
        db.session.add(employee)
        db.session.commit()
        return employee.serialize


class EmployeeSingleResource(Resource):
    def get(self, id):
        employee = Employee.query.get(id)
        return employee.serialize

    def put(self, id):
        data = request.json
        employee = Employee.query.get(id)
        employee.name = data['name'] if data.get('name', False) else employee.name
        employee.email = data['email'] if data.get('email', False) else employee.email
        employee.department_type = data['department_type'] if data.get('department_type', False) else employee.department_type
        employee.department_id = data['department_id'] if data.get('department_id', False) else employee.department_id
        db.session.add(employee)
        db.session.commit()
        return employee.serialize

    def delete(self, id):
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return "", 204


api.add_resource(EmployeeSingleResource, '/api/v1/employees/<int:id>')
api.add_resource(EmployeeResource, '/api/v1/employees')
