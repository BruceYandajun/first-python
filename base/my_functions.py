def my_max(m, n):
    if m > n:
        return m
    else:
        return n


a, b = 4, 6
print((my_max(a, b)))

t = lambda m, n: m if m > n else n

a, b = 1, 3
print(t(a, b))


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ["Geeks", "for", "Geeks"]
myFun(*args)
print("-----------------")
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
