a = 2
type_ = "=="
print(eval(f"a {type_} a"))


def method(n):
    return f"This is {n}"


b = "Bruce"
e = eval(f"method(b)")
print(e)

operator = "+"

c = 1
d = 2
e = eval(f"{c} {operator} d")
print(e)


class User:

    @classmethod
    def hello(cls, name):
        print(f"Hello, {name}")


eval(f"User.hello(b)")


def is_num(_str):
    return str(_str).replace(".", "", 1).isdigit()


s = "123.45"
print(is_num(s))

t = "('a', 'b')"
print(type(eval(t)))

a = ["a", "b", "c"]
print(eval('[{"tt": "abc"}]'))
print(type(eval('[{"tt": "abc"}]')))
