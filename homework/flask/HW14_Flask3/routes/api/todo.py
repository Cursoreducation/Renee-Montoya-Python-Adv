from app import app, api
from flask import request
from flask_restful import Resource, abort

todos = []


class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        todos.append(request.json)
        return todos


class TodoEditor(Resource):
    def get(self, id):
        if 0 <= id < len(todos):
            return todos[id]
        else:
            abort(404, message="Todo {} doesn't exist".format(id))


    def patch(self, id):
        if 0 <= id < len(todos):
            todos[id] = request.json
            return todos
        else:
            abort(404, message="Todo {} doesn't exist".format(id))

    def delete(self, id):
        if 0 <= id < len(todos):
            todos.pop(id)
            return todos
        else:
            abort(404, message="Todo {} doesn't exist".format(id))


api.add_resource(Todo, "/api/v1/todos")
api.add_resource(TodoEditor, "/api/v1/todos/<int:id>")
