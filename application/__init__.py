from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json
import sqlite3

db_file = 'sqlite:///bigpro.db'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_file
db = SQLAlchemy(app)


# DATABASE

class User(db.Model):
    username = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    def toJson(self):
        return {"username": self.username, "password": self.password}

    def __repr__(self):
        return json.dumps(self.__dict__)

db.create_all()

from application import routes