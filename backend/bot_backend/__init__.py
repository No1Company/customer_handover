from flask import Flask, jsonify, request
from datetime import datetime as d

app = Flask(__name__, static_folder = 'static', static_url_path = '/')

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

current_bookings = [
        {
            "bookingdate" : "",
            "type" : ""
        }
    ]

@app.route('/current-bookings', methods=['GET', 'POST'])
def curr_bookings():

    if request.method == "POST":
        
        current_bookings.append(request.get_json())
        print(current_bookings)

    return jsonify([ {"bookingdate": booking["bookingdate"], "type": booking["type"]} for booking in current_bookings])
