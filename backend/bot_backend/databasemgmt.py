from bot_backend.models import *
from bot_backend import app
def resetDB():
    db.init_app(app)
    db.drop_all()
    db.create_all()