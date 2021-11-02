from app import db


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

    @property
    def serialize(self):
        return {
            'id': self.id,
            'location': self.location,
            'name': self.name
        }


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
    name = db.Column(
        db.String(255),
        nullable=False,
    )

    department_type = db.Column(
        db.String(50),
        nullable=False,
    )
    department_id = db.Column(
        db.Integer,
        nullable=False
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'department_type': self.department_type,
            'department_id': self.department_id
        }