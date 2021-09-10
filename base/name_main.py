import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

print("before import")

import math

print("before functionA")


def functionA():
    print("Function A")


print("before functionB")


def functionB():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
