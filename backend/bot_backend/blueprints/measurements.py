from flask import Blueprint, request
from bot_backend.models import db, User, MeasurementForm, RegisteredMeasurement
import json
from datetime import date

measurements = Blueprint('measurements', __name__, url_prefix='/measurements')

@measurements.route('/get-form/<int:id>', methods=['GET'])
def get_form(id):
    return json.loads(MeasurementForm.query.get_or_404(id).form)

@measurements.route('/register-form/<uuid:ehr_id>/<int:id>', methods=['POST'])
def register_form(ehr_id, id):
    User.query.get_or_404(str(ehr_id))
    MeasurementForm.query.get_or_404(id)
    if request.get_json():
        r = RegisteredMeasurement(user=str(ehr_id), form=id, date=date.today(), answers=json.dumps(request.get_json()))
        db.session.add(r)
        db.session.commit()
        return r.serialize(), 200
    else:
        return {'msg': 'wrong fields in json'}, 400
