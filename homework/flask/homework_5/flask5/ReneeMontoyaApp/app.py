from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from wait_for_db import connect_to_db


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object("config.Config")
api = Api(app)
db.init_app(app)


with app.app_context():
    from routes.main import *
    from routes.api.plants import *
    from routes.api.employees import *
    from routes.api.salons import *
    from models import Plant, Employee, Salon

    # connect_to_db(db)
    db.create_all()

app.run(debug=True, host="0.0.0.0", port=8080)