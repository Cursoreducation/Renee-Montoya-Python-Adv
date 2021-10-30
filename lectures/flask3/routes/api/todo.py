from app import app, api
from flask import request
from flask_restful import Resource

todos = []

class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        todos.append(request.json)
        return todos

api.add_resource(Todo, "/api/v1/todos")
