import flask
from _starter import app
from _starter import cache
from _executor import MyExecutor
from init_pool import InitPool

print("init app")


@app.route("/api/das/execute", methods=["GET"])
# @cache.cached()
def execute():
    start = int(flask.request.args.get("start"))
    end = int(flask.request.args.get("end"))
    MyExecutor.execute_parallel(start, end)
    print("execute")
    return "ok"


@app.route("/api/das/cache/clear", methods=["GET"])
def clear():
    cache.clear()
    return "Cache cleared"


if __name__ == "__main__":
    InitPool.init()
    app.run(host="0.0.0.0", port=8080, debug=False)
