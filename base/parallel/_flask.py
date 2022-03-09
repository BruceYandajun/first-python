import flask
import _executor
import _starter
from concurrent.futures import as_completed

app = flask.Flask(__name__)


@app.route("/api/das/execute", methods=["GET"])
def execute():
    result_future1 = {_starter.MyPool.process_pool.submit(_executor.MyExecutor.batch_tasks)}
    print("-----------------------------")
    result_future2 = {_starter.MyPool.process_pool.submit(_executor.MyExecutor.batch_tasks_parallel)}
    r1 = [f.result() for f in as_completed(result_future1)]
    r2 = [f.result() for f in as_completed(result_future2)]
    r3 = r2.append(r1)
    print(r3)
    return "ok"


if __name__ == "__main__":
    _starter.MyPool.init()
    app.run(host="0.0.0.0", port=8080, debug=False)
