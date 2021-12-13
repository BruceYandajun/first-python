a = 2
print(eval("a * a"))


def method(n):
    return f"This is {n}"


b = "Bruce"
e = eval("method(b)")
print(e)

operator = "+"

c = 1
d = 2
e = eval(f"c{operator}d")
print(e)


class User:

    @classmethod
    def hello(cls, name):
        print(f"Hello, {name}")


eval(f"User.hello(b)")

