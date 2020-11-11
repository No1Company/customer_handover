from flask import Blueprint, jsonify, request
import openehr_com as ehr_com

openehr = Blueprint('openehr', __name__, url_prefix='/openehr')

########################################################################
# Generates a fake user and returns json containing data about said
# user. The most important parts of that json object is the ehr-id which
# uniquely identifies a patient.
########################################################################
@openehr.route('/generate-fake-user', methods=['GET'])
def generate_fake_user():
    return ehr_com.generate_fake_user()["party"]

########################################################################
# Route for adding blood pressure measurements to a specified user.
# Should be supplied with a json object containing the fields systolic, 
# diastolic and time. 
########################################################################		
@openehr.route('/add-blood-pressure/<uuid:ehr_id>', methods=['POST'])
def add_blood_pressure(ehr_id):
        json = request.get_json()
        if json['systolic'] and json['diastolic'] and json['time']:
            return ehr_com.add_blood_pressure(ehr_id, json['systolic'], json['diastolic'], json['time'])
        else:
            return {"msg": "missing parameters"}, 400
        
########################################################################
# Gets the blood pressure for a patient specified by the ehr-id.
########################################################################
@openehr.route('get-blood-pressure/<uuid:ehr_id>')
def get_blood_pressure(ehr_id):
    return jsonify(ehr_com.get_blood_pressure(ehr_id))