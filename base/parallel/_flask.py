import flask

from _executor import MyExecutor

app = flask.Flask(__name__)

print("init flask")


@app.route("/api/das/execute", methods=["GET"])
def execute():
    print(MyExecutor.batch_tasks())
    print("---------------------------------------------------------------------------------")
    print(MyExecutor.batch_tasks_parallel())
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
