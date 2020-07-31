from flask import Flask
from flask_restful import Api

from models.user import UserModel
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)

    result = [item.json() for item in UserModel.query.all()]

    print(result)
