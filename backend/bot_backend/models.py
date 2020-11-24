from flask_sqlalchemy import SQLAlchemy
from bot_backend import app
from datetime import date, timedelta
import json
db = SQLAlchemy(app)

def removeSweChars(swe):
    returnList = list(swe)
    charmap = {
        'å': 'a',
        'ä': 'a',
        'ö': 'o'
    }
    for i in range(len(returnList)):
        if returnList[i] in charmap:
            returnList[i] = charmap[returnList[i]]

    return ''.join(returnList)



class User(db.Model):
    __tablename__ = "user"
    ehr_id = db.Column(db.String, primary_key=True)
    measurements = db.relationship("UserMeasurement")
    RegisteredMeasurements = db.relationship("RegisteredMeasurement")

    def __repr__(self):
        return f"<User {self.ehr_id}: >"

    def getAvailableMeasurements(self):
        returnDict = {'avail_measurements' : [m.measurement.name for m in self.measurements if m.next_measurement <= date.today()]}
        for m in self.measurements:
            if m.measurement.form:
                returnDict[f'{removeSweChars(m.measurement.name)}'] = m.measurement.form
        return returnDict

    def getMeasurements(self):
        return [{'name': m.measurement.name, 'next': m.next_measurement.isoformat()} for m in self.measurements]

class UserMeasurement(db.Model):
    __tablename__ = "usermeasurement"
    user_id = db.Column(db.String, db.ForeignKey(
        "user.ehr_id"), primary_key=True)
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
    form = db.Column(db.Integer, db.ForeignKey("measurementform.id"), nullable=True)

    def __repr__(self):
        return f"<Measurement {self.id}: {self.name}>"


class MeasurementForm(db.Model):
    __tablename__ = "measurementform"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    form = db.Column(db.String)

    def __repr__(self):
        return f'<MeasurementForm {self.id}: name={self.name} jsonContent={self.JsonContent}>'


class RegisteredMeasurement(db.Model):
    __tablename__ = "registeredmeasurement"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, db.ForeignKey('user.ehr_id'))
    form = db.Column(db.Integer, db.ForeignKey('measurementform.id'))
    date = db.Column(db.Date)
    answers = db.Column(db.String)
    def __repr__(self):
        return f'<RegisteredMeasurement {self.id}: user={self.user} form={self.form} date={self.date} answers={self.answers}>'

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user,
            'form': self.form,
            'date': self.date,
            'answers': self.answers
        }

    def getFormatted(self):
        answers = json.loads(self.answers)
        form = json.loads(MeasurementForm.query.get(self.form).form)
        return [
            {
                "question": q['question'],
                "avail_answers": q['answer'],
                "answer": a
            }
            for a, q in zip(answers, form['questions'])
        ]
