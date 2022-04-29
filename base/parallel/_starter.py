import os
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Manager
import flask

from flask_cache import Cache

print("init _starter")
app = flask.Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': 'flask-cache'})
print("init flask")


class MyPool:
    thread_pool = None
    process_pool = None

    @classmethod
    def init(cls):
        print("init MyPool")
        cls.thread_pool = ThreadPoolExecutor(max_workers=os.cpu_count())
        print(f"id of thread_pool {id(cls.thread_pool)}")
        cls.process_pool = ProcessPoolExecutor()
        print(f"id of process_pool {id(cls.process_pool)}")
        pass


class MyData:
    df_map = None

    @classmethod
    def init(cls):
        cls.df_map = Manager().dict()
        # cls.df_map = {}
