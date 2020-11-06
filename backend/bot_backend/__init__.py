from flask import Flask
from datetime import datetime

app = Flask(__name__, static_folder = 'static', static_url_path = '/')

@app.route('/')
def main():
    return 'Hello world'

@app.route('/available-times', methods=['GET'])
def avail_times():
    times = [datetime.datetime(2020, 11, 7, 14, 30, 0, tzinfo=datetime.timezone.)]
    return ""