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
            department_id=int(request_data['deparment_id']),
        )
        db.session.add(employee)
        db.session.commit()
        return employee.serialize


class EmployeeSingleResource(Resource):
    def get(self, id):
        employee = Employee.query.get(id)
        return employee.serialize

    # def put(self, id):
    #     data = request.json
    #     Employee.update_by_id(id, data)
    #     return Employee.get_by_id(id)

    def delete(self, id):
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return "", 204


api.add_resource(EmployeeResource, '/api/v1/employees')
api.add_resource(EmployeeSingleResource, '/api/v1/employees/<int:id>')
