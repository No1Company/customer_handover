from flask import Flask

app = Flask(__name__, static_folder = 'static', static_url_path = '/')

@app.route("/")
def main():
    return "Hello world"