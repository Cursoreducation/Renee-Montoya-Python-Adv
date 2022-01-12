from app import app, api
from models import Employee
from flask import request
from flask_restful import Resource


class EmployeeResource(Resource):
    def get(self):
        try:
            employees = Employee.get_all()
            limit = int(request.args.get('limit', False))
            if limit:
                return employees[:limit]
            return employees
        except Exception:
            return "Employees not found", 404

    def post(self):
        try:
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
        except Exception:
            return "Something wrong. Wrong data.", 409


class EmployeeSingleResource(Resource):
    def get(self, id):
        try:
            return Employee.get_by_id(id)
        except Exception:
            return "Single employee not found", 404

    def put(self, id):
        try:
            data = request.json
            Employee.update_by_id(id, data)
            return Employee.get_by_id(id)
        except Exception:
            return "Single employee not found", 404

    def delete(self, id):
        try:
            Employee.delete_by_id(id)
            return "", 204
        except Exception:
            return "Single employee not found", 404


api.add_resource(EmployeeSingleResource, '/api/v1/employees/<int:id>')
api.add_resource(EmployeeResource, '/api/v1/employees')