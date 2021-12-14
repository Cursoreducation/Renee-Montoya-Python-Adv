from app import app, api
from flask import request, Response
from flask_restful import Resource
from models import Salon


class SalonResource(Resource):
    def get(self):
        salons = Salon.get_all()
        limit = int(request.args.get('limit', False))
        if limit:
            return salons[:limit]
        return salons

    def post(self):
        data = request.json
        salon = Salon(data['id'], data['name'], data['director_id'], data['city'], data['address'])
        salon.save()
        return salon._generate_dict()


class SalonSingleResource(Resource):
    def get(self, id):
        return Salon.get_by_id(id)

    def put(self, id):
        data = request.json
        Salon.update_by_id(id, data)
        return Salon.get_by_id(id)

    def delete(self, id):
        Salon.delete_by_id(id)
        return "", 204


class SalonDirectorResource(Resource):
    def get(self, id):
        try:
            salon = Salon.get_by_id(id)
            director = Salon.director(salon['director_id'])
            if director is None:
                return "Director Not Found", 404
            return director
        except Exception:
            return "Not Found", 404


api.add_resource(SalonDirectorResource, '/api/v1/salons/<int:id>/director')
api.add_resource(SalonResource, "/api/v1/salons")
api.add_resource(SalonSingleResource, "/api/v1/salons/<int:id>")
