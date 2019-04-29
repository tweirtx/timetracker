from .signer import sign
import flask

app = flask.Flask('timetracker')


@app.route('/')
def serve_index():
    return flask.send_from_directory('/home/travis/PycharmProjects/timetracker', 'index.html')  # TODO relative path


@app.route("/execute")
def execute():
    args = flask.request.args
    if args.get("user_id") is None:
        return "Error"
    return sign(args.get("user_id"))


@app.route('/report')
def report():
    return "TODO"


def start():
    print("Initializing web interface")
    app.run(host='0.0.0.0')
