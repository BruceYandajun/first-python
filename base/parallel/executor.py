from concurrent.futures.process import ProcessPoolExecutor
import time


def func(a):
    time.sleep(5)
    print(a)
    return a


pool = ProcessPoolExecutor(max_workers=10)

my_list = ["a", "b", "c"]
nums = [i for i in my_list]
if __name__ == "__main__":
    future = pool.submit(func, nums)
    print(future.result())
