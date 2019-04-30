import os
from .signer import sign
from .db import *
from .config import config
import flask
from flask_table import Table, Col

app = flask.Flask('timetracker')


class ReportTable(Table):

    name = Col('Name')
    hours = Col('Hours')
    has_made_hours = Col('Has made hours')


class Report(object):
    def __init__(self, user_report):
        self.name = user_report.name
        self.hours = user_report.minutes / 60
        self.has_made_hours = self.hours >= config['minimum_hours']


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
    report_objects = []
    with Session() as session:
        reports = session.query(Members)
        for user_report in reports:
            report_objects.append(Report(user_report))
    return ReportTable(report_objects, border=True).__html__()


@app.route('/submit.js')
def submit_js():
    return flask.send_from_directory(os.getcwd(), 'submit.js')


def start():
    print("Initializing web interface")
    app.run(host='0.0.0.0')
