import copy


a = [[1, 1, 1], [2, 2, 2]]
b = copy.copy(a)
print(id(a))
print(id(b))
a.append([3, 3, 3])
print(b)
a[1][1] = 5
print(a)
print(b)


c = {
    "fields": [
        "1",
        "2"
    ]
}
d = copy.deepcopy(c)
print(c)
c["fields"][0] = "3"
print(d)
