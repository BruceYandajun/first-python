import sys

try:
    a = 5 / 0
    print(a)
except ArithmeticError:
    print("ArithmeticError error:", sys.exc_info()[0])
except Exception:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("Processed successfully!!!")
finally:
    print("Finally!")
