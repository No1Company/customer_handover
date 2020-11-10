from userdb import db
from userdb import User
#from sqlalchemy import select
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

db.create_all()
#engine = create_engine('sqlite:///users.db', echo = True)
#session = sessionmaker()


# generate users
ehrids = [ "200f9679-d14c-4004-90e9-9f0208cf4158", "04b5dbae-d2ad-4823-837c-61bcea81bafc"]
for i in ehrids:
	email = "test"+str(ehrids.index(i)+1)+"@test.com"
	genuser = User(email=email,ehrid=i)
	genuser.set_password("test")
	db.session.add(genuser)

db.session.commit()


