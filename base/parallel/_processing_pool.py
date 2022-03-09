import os
import time
from multiprocessing import Pool
import pandas as pd
from time_use import log_execution_time


@log_execution_time
def task(n):
    print('{} is running'.format(os.getpid()))
    pd.read_pickle(
        "/Users/yandajun/Documents/pycharm_projects/baidu/acg-airec/das/output/guangda/2022030101/actions.pkl")
    print('{} is done'.format(os.getpid()))
    return n


if __name__ == '__main__':
    # print(os.cpu_count())  #查看cpu个数
    start = time.time()
    ret_lis = []
    p = Pool(7)  # 最大四个进程
    for i in range(1, 7):  # 开7个任务
        ret = p.apply_async(task, args=(i,))  # 异步的
        ret_lis.append(ret)
    p.close()  # 禁止往进程池内在添加任务
    p.join()  # 等待进程池
    # print('主进程')
    print(_.get() for _ in ret_lis)
    # for i in range(1, 7):
    #     task(i)
    end = time.time()
    print(end - start)
