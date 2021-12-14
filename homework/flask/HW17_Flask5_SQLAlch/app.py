from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import pymysql

from utils.check_mysql import check_mysql_connect

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy()
api = Api(app)
if __name__ == '__main__':
    if check_mysql_connect():
        db.init_app(app)

        with app.app_context():
            from routes.main import *
            from routes.api.plants import *
            from routes.api.employees import *
            from routes.api.salons import *
            from models import Plant, Employee, Salon

            db.create_all()

        app.run(debug=True, host="0.0.0.0", port=8080)