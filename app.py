from flask import Flask, request, jsonify
import io
from imageClassification import predict

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the home page!"


@app.route("/test", methods=["GET", "POST"])
def test():
    return jsonify({"preds": [("Class A", 90), ("Class B", 80)]})


@app.route("/imageClassification", methods=["GET", "POST"])
def image_classification():
    file = request.files["file"]
    fileBytes = io.BytesIO(file.read())
    return jsonify({"preds": predict(fileBytes, app.logger)})


if __name__ == "__main__":
    app.run()
