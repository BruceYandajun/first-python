from flask import Flask

app = Flask(__name__)


@app.route("/das/flask/get", methods=["GET"])
def get_():
    return "test"


if __name__ == "__main__":
    app.run(debug=True, port=8285)
