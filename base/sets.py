s1 = {'a', 'b', 'c', 'a'}
print(s1)
print(max(s1))
s2 = {'a', 'b', 'd'}
print(s1 - s2)  # 集合s1中包含s2中不包含的元素
print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)  # 不同时包含于s1和s2的元素

s1 = {"a", "b"}
s2 = {"a", "c"}
print(s1.union(s2))
