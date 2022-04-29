# 列表可以放不同类型的元素
import random

list1 = [1, 'abc', 0.5]
print(list1)
print(list1[0:])
print(list1[0:-1])
print(list1[-3:])
# print(list1[3])  # 越界

list2 = list1 + [2]
print(list2)

list3 = list2[-1::-1]  # 反转数组
print(list3)

print(1 in list1)
for i in list1:
    print(i, end=' ')
print()
m = [1, 5, 3, 3, 4]
print(max(m))
print(m.count(3))
m.reverse()
print(m)

total = 0
myList = [1, 5]
for i in myList:
    total += i
print('Total of myList is %s' % total)

print(random.choice(range(1, 2)))

print(myList)
myList.pop(1)
print(myList)

ll = []
if not ll:
    print("list is empty")
list1 = ["a", "b"]
list2 = ["c", "d"]
list3 = list1 + list2
print(list1)

my_list = [1, 5, 7]
print("01" in my_list)


def eq(a):
    return a > 1


c = filter(eq, [1, 2])
print(c)


def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)