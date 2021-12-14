from app import app, api, db
from flask import request, Response
from flask_restful import Resource
from models import Salon, Employee
from utils.helpers import convert_list


class SalonResource(Resource):
    def get(self):
        plants = Salon.query.all()
        return convert_list(plants)


    def post(self):
        data = request.json
        salon = Salon(name=data['name'],
                      director_id=data['director_id'],
                      city=data['city'],
                      address=data['address'])
        db.session.add(salon)
        db.session.commit()
        return salon.serialize


class SalonSingleResource(Resource):
    def get(self, id):
        plant = Salon.query.get(id)
        return plant.serialize


    def put(self, id):
        data = request.json

        salon = Salon.query.get(id)
        salon.name = data['name']
        salon.city = data['city']
        salon.address = data['address']
        salon.director_id = data['director_id']
        db.session.commit()
        return salon.serialize

    def delete(self, id):
        salon = Salon.query.get(id)
        db.session.delete(salon)
        db.session.commit()
        return "", 204


class SalonDirectorResource(Resource):
    def get(self, id):
        try:
            salon = Salon.query.get(id)
            if salon.director_id:
                director = Employee.query.get(salon.director_id)
                if director is None:
                    return "Director Not Found", 404
                return director.serialize
            return "Director Not Set", 404
        except Exception:
            return "Not Found", 404


api.add_resource(SalonDirectorResource, '/api/v1/salons/<int:id>/director')
api.add_resource(SalonResource, "/api/v1/salons")
api.add_resource(SalonSingleResource, "/api/v1/salons/<int:id>")
