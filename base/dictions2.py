d = {'mike': 10, 'lucy': 2, 'ben': 30}
print(type(d))
_tuple = sorted(d.items(), key=lambda x: x[1], reverse=False)
print(_tuple)


for item in d.items():
    print(item)

for k in d.keys():
    print(f"k={k}")

for v in d.values():
    print(f"v={v}")

for k, v in enumerate(d):
    print(f"k={k}, v={v}")
e = {'mike': 15, 'bruce': 30}
d.update(e)
print(d)
