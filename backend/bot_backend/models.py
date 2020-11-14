from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ehr_id = db.Column(db.String)
    def __repr__(self):
        return "<User {id}: >".format(id = self.id)