from bot_backend.models import *
from datetime import date
import os

import json


def resetDB():
    db.drop_all()
    db.create_all()


def createSmallExample():
    blodtryck = Measurement(name="Blodtryck")
    vikt = Measurement(name="Vikt")
    halsoformular = Measurement(name="Hälsoformulär")

    db.session.add_all([blodtryck,
                        vikt,
                        halsoformular])
    db.session.commit()

    u1 = User(ehr_id='8d27c6c1-0811-4077-bb68-d9759c914cd0')
    u2 = User(ehr_id='5b7610b9-c0b8-44aa-aeff-3f8783a437d9')
    u3 = User(ehr_id='b8f24115-58f9-4d1b-aab4-06fa5e5fad3d')

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    um1 = UserMeasurement(user_id=u1.ehr_id, measurement_id=blodtryck.id,
                          next_measurement=date.today(), interval_days=1)
    um2 = UserMeasurement(user_id=u1.ehr_id, measurement_id=vikt.id,
                          next_measurement=date.today(), interval_days=1)
    um3 = UserMeasurement(user_id=u1.ehr_id, measurement_id=halsoformular.id,
                          next_measurement=date.today(), interval_days=1)
    um4 = UserMeasurement(user_id=u2.ehr_id, measurement_id=blodtryck.id,
                          next_measurement=date.today(), interval_days=7)
    um5 = UserMeasurement(user_id=u3.ehr_id, measurement_id=vikt.id,
                          next_measurement=date.today(), interval_days=30)

    db.session.add_all([um1, um2, um3, um4])
    db.session.commit()

    f = open("FormHealth.txt", 'r')
    form = f.read()
    if (os.name == "nt"):
        form = form.encode('cp1252').decode('utf-8')
    m = json.loads(form)
    mf = MeasurementForm(name="Hälsoformulär", form=json.dumps(m))


    db.session.add(mf)
    db.session.commit()

    halsoformular.form = mf.id
    db.session.commit()

    rm = RegisteredMeasurement(
        user=User.query.get('8d27c6c1-0811-4077-bb68-d9759c914cd0').ehr_id,
        form = mf.id,
        date = date.today(),
        answers = json.dumps(json.loads('[1,2,3,4,5,1,2,3,4,5]'))
        )
    db.session.add(rm)
    db.session.commit()
