from bot_backend.models import db, User, Measurement, UserMeasurement
from datetime import date


def resetDB():
    db.drop_all()
    db.create_all()


def createSmallExample():
    blodtryck = Measurement(name="Blodtryck")
    vikt = Measurement(name="Vikt")

    db.session.add_all([blodtryck,
                        vikt])
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
    um3 = UserMeasurement(user_id=u2.ehr_id, measurement_id=blodtryck.id,
                          next_measurement=date.today(), interval_days=7)
    um4 = UserMeasurement(user_id=u3.ehr_id, measurement_id=vikt.id,
                          next_measurement=date.today(), interval_days=30)

    db.session.add_all([um1, um2, um3, um4])
    db.session.commit()