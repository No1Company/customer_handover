from flask import Flask, jsonify, request
from datetime import datetime as d
import os
import platform


app = Flask(__name__, static_folder = 'static', static_url_path = '/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from bot_backend.blueprints import openehr, user, measurements
app.register_blueprint(openehr.openehr)
app.register_blueprint(user.user)
app.register_blueprint(measurements.measurements)

@app.route('/')
def main():
    return 'Hello world'

@app.route('/available-times', methods=['GET'])
def avail_times():
    times = [
            {
                "start" : d(2020, 12, 14, 14, 30),
                "stop"  : d(2020, 12, 14, 15, 30)
            },

            {
                "start" : d(2020, 12, 15, 11, 0),
                "stop"  : d(2020, 12, 15, 11, 30)
            },
            
            {
                "start" : d(2020, 12, 18, 14, 30),
                "stop"  : d(2020, 12, 18, 15, 30)
            },
            
            {
                "start" : d(2020, 12, 20, 8, 15),
                "stop"  : d(2020, 12, 20, 8, 45)
            },
            
            {
                "start" : d(2020, 12, 22, 10, 30),
                "stop"  : d(2020, 12, 22, 11, 00)
            },
            
            {
                "start" : d(2021, 2, 15, 10, 15),
                "stop"  : d(2021, 2, 15, 10, 45)
            },
            
            {
                "start" : d(2021, 1, 23, 8, 30),
                "stop"  : d(2021, 1, 23, 9, 00)
            }
        ]


    return jsonify([ {"start": time["start"].strftime("%y/%m/%d") + " " + time["start"].strftime("%X")[:-3], "stop": time["stop"].strftime("%y/%m/%d") + " " + time["stop"].strftime("%X")[:-3]} for time in times ])


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
            "type" : "",
            "free-text" : ""
        }
    ]

@app.route('/current-bookings', methods=['GET', 'POST'])
def all_current_bookings():

    if request.method == "POST":
        current_bookings.append(request.get_json())
        return "200"

    elif request.method == "GET":
        return jsonify(current_bookings)

@app.route('/current-bookings/<int:booking_id>', methods=['GET', 'DELETE'])
def specific_current_booking(booking_id):

    if request.method == "GET":
        return jsonify(current_bookings[booking_id])

    elif request.method == "DELETE":
        current_bookings.pop(booking_id)
        return "200"
        
    