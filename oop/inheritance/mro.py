# MRO(Method Resolution Order多重继承方法解析顺序)


class A:
    pass


class B(A):
    pass


class C(B):
    pass


class D(C, A):
    pass


print(D.__mro__)
