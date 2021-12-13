import multiprocessing
import time
from multiprocessing import Pool


pool = Pool(multiprocessing.cpu_count())


def method(day):
    time.sleep(5)
    print(f"{day}")


start = time.time()
threads = []
nums = [i for i in range(1, 10)]

pool.map(method, nums)

for t in threads:
    t.join()

end = time.time()
print(f"Ran {end - start} s")
