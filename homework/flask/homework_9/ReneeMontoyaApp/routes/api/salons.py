from app import app, api, db
from flask import request, Response
from flask_restful import Resource
from models import Salon
from utils.helpers import convert_list


class SalonResource(Resource):
    def get(self):
        salons = Salon.query.all()

        return convert_list(salons)

    def post(self):
        r_data = request.json
        salon = Salon(
            name=r_data['name'],
            city=r_data['city'],
            address=r_data['address']
        )
        db.session.add(salon)
        db.session.commit()
        return salon.serialize


class SalonSingleResource(Resource):
    def get(self, id):
        try:
            salon = Salon.query.get(id)
            return salon.serialize
        except Exception:
            return 'Single salon not found.', 404

    def put(self, id):
        data = request.json

        salon = Salon.query.get(id)
        salon.name = data['name'] if data.get('name', False) else salon.name
        salon.email = data['director_id'] if data.get('director_id', False) else salon.director_id
        salon.city = data['city'] if data.get('city', False) else salon.city
        salon. address = data['address'] if data.get('address', False) else salon.address
        db.session.add(salon)
        db.session.commit()
        return salon.serialize

    def delete(self, id):
        try:
            salon = Salon.query.get(id)
            db.session.delete(salon)
            db.session.commit()
            return f"Salon {id} Deleted", 204
        except Exception:
            return 'Single salon not found.', 404


class SalonDirectorResource(Resource):
    def get(self, id):
        try:
            salon = Salon.get_by_id(id)
            director = Salon.director(salon['director_id'])
            if director is None:
                return "Salon Director Not Found", 404
            return director
        except Exception:
            return "Not Found", 404


api.add_resource(SalonDirectorResource, '/api/v1/salons/<int:id>/director')
api.add_resource(SalonSingleResource, '/api/v1/salons/<int:id>')
api.add_resource(SalonResource, '/api/v1/salons')
