def abc():
    pass


print(abc.__name__)
print(abc.__class__)
print(abc.__doc__)
print(abc.__module__)
print(abc.__qualname__)


class A:

    @staticmethod
    def b():
        print("run")
        pass


print(A.b.__name__)
print(A.b.__class__)
print(A.b.__doc__)
print(A.b.__module__)
print(A.b.__qualname__)
