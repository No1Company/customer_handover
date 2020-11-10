from flask import Flask, jsonify
from datetime import datetime as d
import requests

from bot_backend.blueprints import openehr

app = Flask(__name__, static_folder = 'static', static_url_path = '/')
app.register_blueprint(openehr.openehr)

loginfile = open("login.txt")
username = loginfile.readline()
password = loginfile.readline()

ehrid = "8521e620-d38e-4fd6-9071-f785c2ece9b3"
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

