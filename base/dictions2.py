d = {'mike': 10, 'lucy': 2, 'ben': 30}
d = sorted(d.items(), key=lambda x: x[1], reverse=False)
print(d)
