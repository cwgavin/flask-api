import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    return "Flask API get endpoint running"


if __name__ == "__main__":
    app.run()
