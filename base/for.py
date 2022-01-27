for i in range(0, 5):
    print(i)

print("---------")

integers = [i * i for i in range(5)]
print(integers)
# 以上等价于
ints = []
for i in range(5):
    ints.append(i * i)
print(integers)

a = ['a', ' b', 'c ', ' d ']
for i, v in enumerate(a):
    a[i] = v.strip()
print(a)

my_dict = {i**2: i for i in range(0, 5)}
print(my_dict)
