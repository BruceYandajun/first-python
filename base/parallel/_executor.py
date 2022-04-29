import functools
import sys
import time
from concurrent.futures import as_completed

import numpy as np
import pandas as pd
import os

import _starter
from _starter import cache


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


def get_size_of(obj):
    return f"{sys.getsizeof(obj) / 1024 / 1024} M"


class MyExecutor:

    @classmethod
    @log_execution_time
    def init(cls):
        _starter.MyData.init()
        nums = [i for i in range(1)]
        future_map = _starter.MyPool.process_pool.map(cls.load, nums)
        return [future for future in future_map]
        pass

    @classmethod
    @log_execution_time
    def load(cls, num):
        df = pd.read_pickle("./actions.pkl")
        print(f"df size: {get_size_of(df)}")
        _starter.MyData.df_map[num] = df
        print(f"load spid:{os.getpid()}")
        return num

    @classmethod
    @log_execution_time
    def cal(cls, num):
        df = _starter.MyData.df_map[num]
        if df is None:
            return
        df = df.groupby("day").agg(pv=("actionType", np.count_nonzero), uv=("deviceId", "nunique"))
        print(f"cal pid:{os.getpid()}")
        return df.to_dict(orient="index")

    @classmethod
    # @log_execution_time
    @cache.memoize(timeout=60)
    def cal_by_disk(cls, num):
        print(f"num: {num}")
        file_path = "./actions.pkl"
        if not os.path.exists(file_path):
            return
        df = pd.read_pickle("./actions.pkl")
        if df is None:
            return
        df = df.groupby("day").agg(pv=("actionType", np.count_nonzero), uv=("deviceId", "nunique"))
        print("cal_by_disk")
        return df.to_dict(orient="index")

    @classmethod
    @log_execution_time
    def execute_parallel(cls, start, end):
        nums = [i for i in range(start, end)]
        futures = _starter.MyPool.process_pool.map(cls.cal_by_disk, nums)
        result_list = [future for future in futures]
        # result_list = [cls.cal_by_disk(num=num) for num in nums]
        # print(result_list)
        return result_list
