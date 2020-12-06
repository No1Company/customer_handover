from flask import Blueprint, jsonify, request
from bot_backend.models import db, User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('<uuid:ehr_id>/available-measurements', methods=['GET'])
def available_measurements(ehr_id):
    u = User.query.get_or_404(str(ehr_id))
    return jsonify(u.getAvailableMeasurements())

@user.route('<uuid:ehr_id>/measurements')
def measurements(ehr_id):
    u = User.query.get_or_404(str(ehr_id))
    return jsonify(u.getMeasurements())