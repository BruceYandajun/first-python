import ujson


my_dict = {"a": 1, "b": "b"}
print(type(my_dict))
json_str = ujson.dumps(my_dict)
print(type(json_str))
print(json_str)
new_dict = ujson.loads(json_str)
print(type(new_dict))
print(new_dict)
