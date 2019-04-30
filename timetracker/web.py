import os
from .signer import sign
import flask

app = flask.Flask('timetracker')


@app.route('/')
def serve_index():
    return flask.send_from_directory(os.getcwd(), 'index.html')


@app.route("/execute", methods=['POST'])
def execute():
    args = flask.request.form.to_dict()
    if not args.get('user_id'):
        return "Error, no user ID found in request"
    return sign(args.get("user_id"))


@app.route('/report')
def report():
    return "TODO"


@app.route('/submit.js')
def submit_js():
    return flask.send_from_directory(os.getcwd(), 'submit.js')


def start():
    print("Initializing web interface")
    app.run(host='0.0.0.0')
