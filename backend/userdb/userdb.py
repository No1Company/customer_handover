from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

#----------==========DB START==========----------#


# User
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	ehrid = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	passw_hash = db.Column(db.String, nullable=True)

	def __repr__(self):
		return '<User %r>' % self.email

	def serialize(self):
		return dict(ehrid=self.ehrid, name=self.name, email=self.email)

	def set_password(self, password):
		self.passw_hash=bcrypt.generate_password_hash(password).decode('utf8')

	def set_ehrid(self, ehrid):
		self.ehrid=ehrid

