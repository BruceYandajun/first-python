import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures import as_completed

pool = ProcessPoolExecutor()


def func(num, b):
    time.sleep(5)
    print(f"num={num}, b={b}")
    return num


def main():
    nums = [i for i in range(5)]
    a = 5
    fs = {pool.submit(func, num, a) for num in nums}
    results = [f.result() for f in as_completed(fs)]
    print(results)
    return results


if __name__ == "__main__":
    future = pool.submit(main)
    print(future.result())
