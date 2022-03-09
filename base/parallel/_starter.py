from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
import os

print("init _starter")


class MyPool:
    print("init MyPool")
    thread_pool = ThreadPoolExecutor(max_workers=os.cpu_count())
    print(f"id of thread_pool {id(thread_pool)}")
    process_pool = ProcessPoolExecutor(max_workers=10)
    print(f"id of process_pool {id(process_pool)}")

    @classmethod
    def init(cls):
        pass
