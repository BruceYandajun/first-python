class CustomException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message


def my_method(n):
    if n == 1:
        raise CustomException(2, "Occurred 1 error")
    elif n == 2:
        raise CustomException(1, "Occurred 2 errors")
    else:
        raise Exception(1, "abc")


if __name__ == "__main__":
    try:
        my_method(3)
    except CustomException as ce:
        print(ce)
    except Exception as e:
        print(e)

