from concurrent.futures.process import ProcessPoolExecutor
import time
from concurrent.futures import as_completed


def func(a):
    time.sleep(5)
    print(a)
    return a


pool = ProcessPoolExecutor()

my_list = ["a", "b", "c"]
nums = [i for i in my_list]
if __name__ == "__main__":
    future_map = [pool.submit(func, num) for num in nums]
    result = [r for r in as_completed(future_map)]
    print(result)
