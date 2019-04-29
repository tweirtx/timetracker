from .signer import sign
import flask

app = flask.Flask('timetracker')


@app.route('/')
def serve_index():
    return flask.send_from_directory('/home/travis/PycharmProjects/timetracker', 'index.html')  # TODO relative path


@app.route("/execute", methods=['POST'])
def execute():
    args = flask.request.form.to_dict()
    print(args)
    if not args.get('user_id'):
        return "Error"
    return sign(args.get("user_id"))


@app.route('/report')
def report():
    return "TODO"


def start():
    print("Initializing web interface")
    app.run(host='0.0.0.0')
