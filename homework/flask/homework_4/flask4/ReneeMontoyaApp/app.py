from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

with app.app_context():
    from routes.main import *
    from routes.api.plants import *
    from routes.api.employees import *
    from routes.api.salons import *

app.run(debug=True)