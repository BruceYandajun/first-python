import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


def functionA():
    print("a1")
    from name_main2 import functionB
    print("a2")
    functionB()
    print("a3")


def functionB():
    print("b")


print("t1")
if __name__ == '__main__':
    print("m1")
    functionA()
    print("m2")
print("t2")
