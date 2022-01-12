from app import db
import json


class Plant(db.Model):
    __tablename__ = "plants"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    location = db.Column(
        db.String(120),
        nullable=False
    )
    name = db.Column(
        db.String(255),
        nullable=False
    )
    director_id = db.Column(
        db.Integer,
        db.ForeignKey('employees.id'),
        nullable=True
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'location': self.location,
            'name': self.name
        }

    director = db.relationship('Employee', foreign_keys=[director_id])

    def __repr__(self):
        return json.dumps(self.serialize)


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    email = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )
    password = db.Column(
        db.String(255),
        nullable=False
    )
    name = db.Column(
        db.String(255),
        nullable=False,
    )
    department_type = db.Column(
        db.String(50),
        nullable=True,
    )
    department_id = db.Column(
        db.Integer,
        db.ForeignKey('plants.id'),
        nullable=False,
    )

    department = db.relationship('Plant', foreign_keys=[department_id])

    @property
    def get_department(self):
        if self.department_type == "salon":
            return Salon.query.get(self.department_id)
        else:
            return self.department

    def __repr__(self):
        return json.dumps(self.serialize)

    def __str__(self):
        return json.dumps(self.serialize)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'department_type': self.department_type,
            'department_id': self.department_id
        }


class Salon(db.Model):
    __tablename__ = "salon"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(255),
        nullable=False,
    )
    director_id = db.Column(
        db.Integer,
        nullable=False
    )
    city = db.Column(
        db.String(255),
        nullable=False,
    )
    address = db.Column(
        db.String(255),
        nullable=False,
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
        }


class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(30),
        nullable=False,
    )
    link = db.Column(
        db.String(400),
        nullable=False,
    )
    is_active = db.Column(
        db.Boolean,
        default=True
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
        }
