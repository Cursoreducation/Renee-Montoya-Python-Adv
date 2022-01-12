from app import app, api, db
from flask import request, Response
from flask_restful import Resource
from models import Salon
from utils.helpers import convert_list


class SalonResource(Resource):
    def get(self):
        try:
            salons = Salon.query_all()
            return convert_list(salons)
        except Exception:
            return 'Salon not found', 404

    def post(self):
        try:
            data = request.json
            salon = Salon(name=data['name'], director_id=data['director_id'], city=data['city'], address=data['address'])
            db.session.add(salon)
            db.session.commit()
            return salon.serialize
        except Exception:
            return 'Something get wrong. Wrong data.', 409


class SalonSingleResource(Resource):
    def get(self, id):
        try:
            salon = Salon.query.get(id)
            return salon.serialize
        except Exception:
            return 'Single salon not found.', 404

    # def put(self, id):
    #     try:
    #         data = request.json
    #         Salon.update_by_id(id, data)
    #         return Salon.get_by_id(id)
    #     except Exception:
    #         return 'Single salon not found.', 404

    def delete(self, id):
        try:
            salon = Salon.query.get(id)
            db.session.delete(salon)
            db.session.commit()
            return f"Salon {id} Deleted", 204
        except Exception:
            return 'Single salon not found.', 404


api.add_resource(SalonResource, '/api/v1/salons')
api.add_resource(SalonSingleResource, '/api/v1/salons/<int:id>')
