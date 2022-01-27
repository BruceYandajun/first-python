import numbers
import copy

a = 5
b = 5.0
c = 10000008989893909
d = eval("1.0")
e = "1.0"

print(isinstance(a, numbers.Number))
print(isinstance(b, numbers.Number))
print(isinstance(c, numbers.Number))
print(type(c))
print(isinstance(d, numbers.Number))
print(type(d))
print(isinstance(e, numbers.Number))
print(type(e))
