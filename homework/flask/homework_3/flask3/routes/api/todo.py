from app import app, api
from flask import request, abort
from flask_restful import Resource

todos = []


class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        req = request.json
        for el in todos:
            if el['title'] == req['title']:
                abort(500, message=f"Todo {el['title']} doesn't exist")
        todos.append(req)
        return todos

    def patch(self):
        req = request.json
        print(req)
        for idx, item in enumerate(todos):
                if item['title'] == req['title']:
                    todos[idx] = req
        print(todos)
        return todos

    def delete(self):
        req = request.json
        for idx, item in enumerate(todos):
            if item['title'] == req['title']:
                todos.pop(idx)
        return todos


api.add_resource(Todo, "/api/v1/todos")
