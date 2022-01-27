import json


my_dict = [{"a": 1, "b": "b"}]
print(type(my_dict))
json_str = json.dumps(my_dict)
print(type(json_str))
print(json_str)
new_dict = json.loads(json_str)
print(type(new_dict))
print(new_dict)

json1 = {"b": {"c": "h"}, "a": 1, }
json2 = {"a": 1, "b": {"c": "h"}}
print(hash(json.dumps(json1)) == hash(json.dumps(json2)))
