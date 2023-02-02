import json
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="欢迎接口")
def hello():
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/openapi.json")
def open_api():
    with open("api.json", "r") as api:
        return json.load(api)
