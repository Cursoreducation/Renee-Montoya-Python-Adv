from app import app, api
from flask import request, Response
from flask_restful import Resource
from models import Plant


class PlantResource(Resource):
    def get(self):
        try:
            plants = Plant.get_all()
            limit = int(request.args.get('limit', False))
            if limit:
                return plants[:limit]
            return plants
        except Exception:
            return "Plants error", 404

    def post(self):
        try:
            data = request.json
            plant = Plant(data['id'], data['location'], data['name'], data['director_id'])
            plant.save()
            return plant._generate_dict()
        except Exception:
            return "Something get wrong. Wrong data.", 404


class PlantSingleResource(Resource):
    def get(self, id):
        try:
            return Plant.get_by_id(id)
        except Exception:
            return "Not Found plant error", 404

    def put(self, id):
        data = request.json
        Plant.update_by_id(id, data)
        return Plant.get_by_id(id)

    def delete(self, id):
        try:
            Plant.delete_by_id(id)
            return "Deleted", 204
        except Exception:
            return "Single plant not found", 404


class PlantDirectorResource(Resource):
    def get(self, id):
        try:
            plant = Plant.get_by_id(id)
            director = Plant.director(plant['director_id'])
            if director is None:
                return "Director Not Found", 404
            return director
        except Exception:
            return "Not Found", 404


api.add_resource(PlantDirectorResource, '/api/v1/plants/<int:id>/director')
api.add_resource(PlantResource, "/api/v1/plants")
api.add_resource(PlantSingleResource, "/api/v1/plants/<int:id>")
