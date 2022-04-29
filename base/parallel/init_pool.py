import _starter
import _executor


class InitPool:

    @classmethod
    def init(cls):
        _starter.MyPool.init()
        _executor.MyExecutor.init()

