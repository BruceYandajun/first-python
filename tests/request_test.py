import requests
import ujson

url = "http://10.137.16.158/airec/v1/dsldemo"
r = requests.post(url, json=ujson.dumps({"args": {"query": ""}}))
print(ujson.loads(r.text))
