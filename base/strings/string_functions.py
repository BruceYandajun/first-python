
print('abc'.upper())
print('abc'.lower())
print('abc'.capitalize())
print(min('abc'))
print('hello world'.title())
print('abc'.split())

print("Number is " + "5")
print("Number is {}".format(5))
print("Number is %d" % 5)
print("Number", "is", 5)

name = "Harry"
age = 5
s = f"{name} is {age} years old."
print(s)
print(f"{5 * 5}")


def greet(n):
    print("Hello, " + n)


print(f"{greet(name)}")
string = "Abc is an educational company."
print(F"{string.title()}")


print(f"Hello, \'{name}\'")

person = {"name": "John", "age": 19}
print(f"{person['name']} is {person['age']} years old.")
