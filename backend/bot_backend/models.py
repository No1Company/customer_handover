from flask_sqlalchemy import SQLAlchemy
from bot_backend import app
from datetime import date, timedelta
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    ehr_id = db.Column(db.String, primary_key=True)
    measurements = db.relationship("UserMeasurement")

    def __repr__(self):
        return f"<User {self.ehr_id}: >"

    def getAvailableMeasurements(self):
        return [m.measurement.name for m in self.measurements if m.next_measurement <= date.today()]

    def getMeasurements(self):
        return [{'name': m.measurement.name , 'next': m.next_measurement.isoformat()} for m in self.measurements]

class UserMeasurement(db.Model):
    __tablename__ = "usermeasurement"
    user_id = db.Column(db.String, db.ForeignKey("user.ehr_id"), primary_key=True)
    measurement_id = db.Column(db.Integer, db.ForeignKey(
        "measurement.id"), primary_key=True)
    next_measurement = db.Column(db.Date)
    interval_days = db.Column(db.Integer, nullable=False)
    measurement = db.relationship("Measurement")

    def __repr__(self):
        return f"<UserMeasurement uid={self.user_id} mid={self.measurement_id}: next_measurement={self.next_measurement}, interval_days={self.interval_days}, name={self.measurement.name} >"

    def updateTime(self):
        td = timedelta(days=self.interval_days)
        self.next_measurement = self.next_measurement + td


class Measurement(db.Model):
    __tablename__ = "measurement"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Measurement {self.id}: {self.name}>"
