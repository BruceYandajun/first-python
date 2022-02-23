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

my_dict = {i ** 2: i for i in range(0, 5)}
print(my_dict)

nums = [1, 5, 6]
nums = [x for x in nums if x > 5]
print(nums)

a = [1, 4, 7]
b = [2, 4, 7, 5]
equal_nums = [(x, y) for x in a for y in b if x == y]
print(equal_nums)
print(list(zip(a, b)))
