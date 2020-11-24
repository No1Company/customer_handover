from flask import Blueprint, jsonify, request
import openehr_com as ehr_com
from datetime import datetime, date
from bot_backend.models import db, User, Measurement, UserMeasurement

openehr = Blueprint('openehr', __name__, url_prefix='/openehr')

########################################################################
# Generates a fake user and returns json containing data about said
# user. The most important parts of that json object is the ehr-id which
# uniquely identifies a patient.
########################################################################


@openehr.route('/generate-fake-user', methods=['GET'])
def generate_fake_user():
    user = ehr_com.generate_fake_user()["party"]
    u = User(ehr_id=user['additionalInfo']['ehrId'])
    db.session.add(u)
    db.session.commit()

    um_arr = []
    for m in Measurement.query.all():
        um_arr.append(UserMeasurement(user_id=u.ehr_id, measurement_id=m.id,
                                      next_measurement=date.today(), interval_days=1))

    db.session.add_all(um_arr)
    db.session.commit()
    return user

########################################################################
# Gets the user with the specified ehr_id.
########################################################################


@openehr.route('get-user/<uuid:ehr_id>', methods=['get'])
def get_user(ehr_id):
    u = User.query.get_or_404(ehr_id)
    u_ehr = ehr_com.get_user(u.ehr_id)
    return u_ehr


########################################################################
# Route for adding blood pressure measurements to a specified user.
# Should be supplied with a json object containing the fields systolic,
# diastolic and time.
########################################################################
@openehr.route('/add-blood-pressure/<uuid:ehr_id>', methods=['POST'])
def add_blood_pressure(ehr_id):
    json = request.get_json()
    if json['systolic'] and json['diastolic']:
        u = User.query.get_or_404(str(ehr_id))
        for m in u.measurements:
            if m.measurement.name == "Blodtryck":
                m.updateTime()
                db.session.commit()
        return ehr_com.add_blood_pressure(ehr_id, json['systolic'], json['diastolic'], datetime.now())
    else:
        return {"msg": "missing parameters"}, 400


########################################################################
# Route for adding weight measurements to a specified user.
# Should be supplied with a json object containing the field "weight".
########################################################################
@openehr.route('/add-weight/<uuid:ehr_id>', methods=['POST'])
def add_weight(ehr_id):
    json = request.get_json()
    if json['weight']:
        u = User.query.get_or_404(str(ehr_id))
        for m in u.measurements:
            if m.measurement.name == "Vikt":
                m.updateTime()
                db.session.commit()
        return ehr_com.add_weight(ehr_id, json['weight'], datetime.now())
    else:
        return {"msg": "missing parameters"}, 400

########################################################################
# Gets the blood pressure for a patient specified by the ehr-id.
########################################################################


@openehr.route('get-blood-pressure/<uuid:ehr_id>')
def get_blood_pressure(ehr_id):
    return jsonify(ehr_com.get_blood_pressure(ehr_id))

########################################################################
# Gets the blood pressure for a patient specified by the ehr-id.
########################################################################
@openehr.route('get-weight/<uuid:ehr_id>')
def get_weight(ehr_id):
    return jsonify(ehr_com.get_weight(ehr_id))
