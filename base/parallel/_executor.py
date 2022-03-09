import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed
import os
import pandas as pd
import functools
import numpy as np
import _starter

print("init executor")


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
    def init(cls):
        _starter.MyPool.init()
        # cls.batch_tasks_parallel()

    @classmethod
    @log_execution_time
    def task(cls, num):
        """
        单个子任务
        """
        # print(f"Task {num} running")
        # 下载文件到本地
        # wget "http://10.137.16.163:8811/data/government/das/data/2022030101/actions.pkl"
        df = pd.read_pickle("/Users/yandajun/Documents/pycharm_projects/first-python/base/parallel/actions.pkl")
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
        future_map = {_starter.MyPool.process_pool.submit(cls.task, num) for num in nums}
        result_list = [future.result() for future in as_completed(future_map)]
        return result_list


if __name__ == "__main__":
    _starter.MyPool.init()
    print(MyExecutor.batch_tasks())
    print("---------------------------------------------------------------------------------")
    print(MyExecutor.batch_tasks_parallel())
