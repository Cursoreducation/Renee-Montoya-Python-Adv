from app import app, api
from flask import request, Response
from flask_restful import Resource
from models import Salon


class SalonResource(Resource):
    def get(self):
        try:
            salons = Salon.get_all()
            limit = int(request.args.get('limit', False))
            if limit:
                return salons[:limit]
            return salons
        except Exception:
            return 'Salon not found', 404

    def post(self):
        try:
            data = request.json
            salon = Salon(data['id'], data['name'], data['director_id'], data['city'], data['address'])
            salon.save()
            return salon._generate_dict()
        except Exception:
            return 'Something get wrong. Wrong data.', 409


class SalonSingleResource(Resource):
    def get(self, id):
        try:
            return Salon.get_by_id(id)
        except Exception:
            return 'Single salon not found.', 404

    def put(self, id):
        try:
            data = request.json
            Salon.update_by_id(id, data)
            return Salon.get_by_id(id)
        except Exception:
            return 'Single salon not found.', 404

    def delete(self, id):
        try:
            Salon.delete_by_id(id)
            return "Deleted error", 204
        except Exception:
            return 'Single salon not found.', 404


api.add_resource(SalonSingleResource, '/api/v1/salons/<int:id>')
api.add_resource(SalonResource, '/api/v1/salons')
