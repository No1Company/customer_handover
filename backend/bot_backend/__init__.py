from flask import Flask, jsonify, request
from datetime import datetime as d
import pickle
import os


app = Flask(__name__, static_folder = 'static', static_url_path = '/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from bot_backend.blueprints import openehr

#db.init_app(app)
app.register_blueprint(openehr.openehr)
cwd_data_path = os.getcwd() + "\\bot_backend\data\data.txt"
DATA_PATH = os.path.abspath(cwd_data_path)

def save_data(data, data_path):
    file = open(data_path, 'wb')
    pickle.dump(data, file)
    file.close()

def load_data(data_path):
    
    try: 
        file = pickle.load(open(data_path, 'rb'))
    except EOFError:
        file = []
    
    return file

@app.route('/')
def main():
    return 'Hello world'

@app.route('/available-times', methods=['GET'])
def avail_times():
    times = [
            {
                "start" : d(2020, 11, 7, 14, 30, 0),
                "stop"  : d(2020, 11, 7, 15, 30, 0)
            },

            {
                "start" : d(2020, 11, 8, 11, 0, 0),
                "stop"  : d(2020, 11, 8, 11, 30, 0)
            },
            
            {
                "start" : d(2020, 11, 8, 14, 30, 0),
                "stop"  : d(2020, 11, 8, 15, 30, 0)
            },
            
            {
                "start" : d(2020, 11, 9, 8, 15, 0),
                "stop"  : d(2020, 11, 9, 8, 45, 0)
            },
            
            {
                "start" : d(2020, 11, 9, 10, 30, 0),
                "stop"  : d(2020, 11, 9, 11, 00, 0)
            }
        ]


    return jsonify([ {"start": time["start"].isoformat(), "stop" : time["stop"].isoformat()} for time in times ])


userguidetypes = [
    {
        "guidetype" : "0"
    }
]

@app.route('/guide-type', methods=['GET', 'PUT'])
def curr_user_guide_type():

    global userguidetype

    if request.method == "PUT":
        userguidetypes[0] = request.get_json()

    return jsonify([{"guidetype": guides["guidetype"]} for guides in userguidetypes])

notifications = [
    {
        "noticemediatype" : "",
        "timeafter" : "",
        "timebefore" : "", 
        "type" : ""
    }
]



@app.route('/current-notifications', methods=['GET', 'POST', 'PUT'])
def curr_notifications():

    

    if request.method == "POST":
        
        notifications.append(request.get_json())
        print(notifications)

    if request.method == "PUT":
        notifications[0] = request.get_json()


    return jsonify([ {"type": notification["type"], "timeafter": notification["timeafter"],
     "timebefore": notification["timebefore"], "noticemediatype": notification["noticemediatype"]} for notification in notifications])


current_bookings = [
        {
            "bookingdate" : "",
            "type" : ""
        }
    ]

@app.route('/current-bookings', methods=['GET', 'POST'])
def all_current_bookings():
    
    current_bookings = load_data(DATA_PATH)

    if request.method == "POST":
        current_bookings.append(request.get_json())
        save_data(current_bookings, DATA_PATH)
        print(current_bookings)
        return "200"

    elif request.method == "GET":
        return jsonify(current_bookings)

@app.route('/current-bookings/<int:booking_id>', methods=['GET', 'DELETE'])
def specific_current_booking(booking_id):

    current_bookings = load_data(DATA_PATH)

    if request.method == "GET":
        return jsonify(current_bookings[booking_id])

    elif request.method == "DELETE":
        current_bookings.pop(booking_id)
        save_data(current_bookings, DATA_PATH)
        return "200"
        
    