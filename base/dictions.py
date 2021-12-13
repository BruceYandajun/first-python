import random

d = {'a': 10, 'b': 20}
print(d)
print(d['a'])
d['a'] = 11
print(d)
for s in d:
    print(s)
    print(d[s])


del d['b']
print(d.values())

d.clear()
print(d)

my_dict = {"a": 1, "b": 1}
group_dict = {"groups": my_dict}
for key in my_dict:
    print(f"{key}-{my_dict[key]}")

print(random.choice(list(my_dict.keys())))
