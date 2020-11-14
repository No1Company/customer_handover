from flask_sqlalchemy import SQLAlchemy
from bot_backend import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "<User {id}: >".format(id = self.id)