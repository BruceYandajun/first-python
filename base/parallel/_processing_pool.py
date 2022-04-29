import multiprocessing
import os
import time
from multiprocessing import Pool
import pandas as pd
from time_use import log_execution_time


@log_execution_time
def task(q):
    df = q.get()
    print(df)
    pd.read_pickle("./actions.pkl")
    return q.qsize()


if __name__ == '__main__':
    # print(os.cpu_count())  #查看cpu个数
    start = time.time()
    queue = multiprocessing.Queue()
    queue.put("a")
    with Pool(os.cpu_count()) as pool:
        res = pool.apply_async(task, args=(queue,))
        print(res)
    end = time.time()
    print(f"main took {end - start} s")

