from flask import Flask, request
import io
from imageClassification import predict

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask API get endpoint running"


@app.route("/test", methods=["GET", "POST"])
def image_classification():
    file = request.files["file"]
    fileBytes = io.BytesIO(file.read())
    return predict(fileBytes, app.logger)


if __name__ == "__main__":
    app.run()
