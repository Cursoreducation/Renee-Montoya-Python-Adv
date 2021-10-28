from app import app, api
from models import Employee
from flask import request
from flask_restful import Resource


class EmployeeResource(Resource):
    def get(self):
        employees = Employee.get_all()
        limit = int(request.args.get('limit', False))
        if limit:
            return employees[:limit]
        return employees

    def post(self):
        request_data = request.json
        employee = Employee(
            request_data['id'],
            request_data['name'],
            request_data['email'],
            request_data['department_type'],
            request_data['deparment_id'],
        )
        employee.save()
        return employee._generate_dict()


class EmployeeSingleResource(Resource):
    def get(self, id):
        return Employee.get_by_id(id)

    def put(self, id):
        data = request.json
        Employee.update_by_id(id, data)
        return Employee.get_by_id(id)

    def delete(self, id):
        Employee.delete_by_id(id)
        return "", 204


api.add_resource(EmployeeSingleResource, '/api/v1/employees/<int:id>')
api.add_resource(EmployeeResource, '/api/v1/employees')