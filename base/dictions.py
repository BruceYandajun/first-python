d = {'a': 10, 'b': 20}
print(d)
print(d['a'])
d['a'] = 11
print(d)

del d['b']
print(d.values())

d.clear()
print(d)
