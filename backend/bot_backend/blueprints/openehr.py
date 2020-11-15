from flask import Blueprint, jsonify, request
import openehr_com as ehr_com
from datetime import datetime
from bot_backend.models import db, User

openehr = Blueprint('openehr', __name__, url_prefix='/openehr')

########################################################################
# Generates a fake user and returns json containing data about said
# user. The most important parts of that json object is the ehr-id which
# uniquely identifies a patient.
########################################################################


@openehr.route('/generate-fake-user', methods=['GET'])
def generate_fake_user():
    user = ehr_com.generate_fake_user()["party"]
    print(user)
    u = User(ehr_id = user['additionalInfo']['ehrId'])
    db.session.add(u)
    db.session.commit()
    user["db_id"] = u.id
    return user

@openehr.route('get-user/<int:id>', methods=['get'])
def get_user(id):
    u = User.query.get_or_404(id)
    u_ehr = ehr_com.get_user(u.ehr_id)
    u_ehr["db_id"] = id
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
        return ehr_com.add_blood_pressure(ehr_id, json['systolic'], json['diastolic'], datetime.now())
    else:
        return {"msg": "missing parameters"}, 400

########################################################################
# Gets the blood pressure for a patient specified by the ehr-id.
########################################################################


@openehr.route('get-blood-pressure/<uuid:ehr_id>')
@openehr.route('get-blood-pressure/<uuid:ehr_id>')
def get_blood_pressure(ehr_id):
    return jsonify(ehr_com.get_blood_pressure(ehr_id))
