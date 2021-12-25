import json


my_dict = [{"a": 1, "b": "b"}]
print(type(my_dict))
json_str = json.dumps(my_dict)
print(type(json_str))
print(json_str)
new_dict = json.loads(json_str)
print(type(new_dict))
print(new_dict)
