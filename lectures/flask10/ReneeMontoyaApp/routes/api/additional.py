from app import db, app, api
from flask_restful import Resource
from sqlalchemy import or_
from flask import request
from models import MenuItem, Employee, Plant
from utils.helpers import convert_list


class MenuItemResource(Resource):
    def get(self):
        menu_items = MenuItem.query.all()
        return convert_list(menu_items)

    def post(self):
        request_data = request.json
        menu_item = MenuItem(
            name = request_data['name'],
            link = request_data['link'],
            is_active=request_data['is_active']
        )
        db.session.add(menu_item)
        db.session.commit()
        return menu_item.serialize


class MenuItemSingleResource(Resource):
    def put(self, id):
        menu_item = MenuItem.query.get(id)
        menu_item.name = request.json['name'] if request.json.get('name', False) else menu_item.name
        menu_item.link = request.json['link'] if request.json.get('link', False) else menu_item.link
        menu_item.is_active = request.json['is_active'] if request.json.get('is_active', False) else menu_item.is_active
        db.session.add(menu_item)
        db.session.commit()
        return menu_item.serialize


class SearchResource(Resource):
    def get(self):
        q = request.args.get('q')
        employees = Employee.query.filter(or_(Employee.name.ilike(f'%{q}%'), Employee.email.ilike(f'%{q}%'))).all()
        print(employees)
        plants = Plant.query.filter(or_(Plant.name.ilike(f'%{q}%'), Plant.location.ilike(f'%{q}%'))).all()
        return convert_list(employees + plants)


api.add_resource(MenuItemResource, '/api/v1/menu-items')
api.add_resource(MenuItemSingleResource, '/api/v1/menu-items/<int:id>')
api.add_resource(SearchResource, '/api/v1/search')
