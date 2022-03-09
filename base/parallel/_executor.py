import functools
import os
import time
from concurrent.futures import as_completed
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

import numpy as np
import pandas as pd

print("init executor")
thread_pool = ThreadPoolExecutor(max_workers=os.cpu_count())
print(f"id of thread_pool {id(thread_pool)}")
process_pool = ProcessPoolExecutor(max_workers=10)
print(f"id of process_pool {id(process_pool)}")


def log_execution_time(func):
    """
    装饰器，计算方法执行时间
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper


class MyExecutor:

    @classmethod
    @log_execution_time
    def task(cls, num):
        """
        单个子任务
        """
        # print(f"Task {num} running")
        # 下载文件到本地
        # wget "http://10.137.16.163:8811/data/government/das/data/2022030101/actions.pkl"
        df = pd.read_pickle(
            "/Users/yandajun/Documents/pycharm_projects/baidu/acg-airec/das/output/guangda/2022030101/actions.pkl")
        # 计算基础指标
        df = df.groupby("day").agg(pv=("actionType", np.count_nonzero), uv=("deviceId", "nunique"))
        return df.to_dict(orient="index")

    @classmethod
    @log_execution_time
    def batch_tasks(cls):
        """
        批量执行任务
        """
        nums = [i for i in range(10)]
        result_list = [cls.task(num) for num in nums]
        return result_list

    @classmethod
    @log_execution_time
    def batch_tasks_parallel(cls):
        """
        批量并发执行任务
        """
        nums = [i for i in range(10)]
        future_map = {process_pool.submit(cls.task, num) for num in nums}
        result_list = [future.result() for future in as_completed(future_map)]
        return result_list


if __name__ == "__main__":
    print(MyExecutor.batch_tasks())
    print("---------------------------------------------------------------------------------")
    print(MyExecutor.batch_tasks_parallel())
