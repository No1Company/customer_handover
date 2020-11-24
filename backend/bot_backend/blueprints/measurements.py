from flask import Blueprint, request, jsonify
from bot_backend.models import db, User, MeasurementForm, RegisteredMeasurement
import json
from datetime import date

measurements = Blueprint('measurements', __name__, url_prefix='/measurements')

@measurements.route('/get-form/<int:id>', methods=['GET'])
def get_form(id):
    a = json.loads(MeasurementForm.query.get_or_404(id).form)
    return json.dumps(a, ensure_ascii=False)

@measurements.route('/register-form/<uuid:ehr_id>/<int:id>', methods=['POST'])
def register_form(ehr_id, id):
    u = User.query.get_or_404(str(ehr_id))
    for m in u.measurements:
        if m.measurement.name == "Hälsoformulär":
            m.updateTime()
            db.session.commit()
    MeasurementForm.query.get_or_404(id)
    if request.get_json():
        r = RegisteredMeasurement(user=str(ehr_id), form=id, date=date.today(), answers=json.dumps(request.get_json(), ensure_ascii=False))
        db.session.add(r)
        db.session.commit()
        return r.serialize(), 200
    else:
        return {'msg': 'wrong fields in json'}, 400
