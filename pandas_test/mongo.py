import pandas as pd
import time
import modin.pandas as mpd
import ray


@ray.remote(num_cpus=4)
def my_test():
    df = pd.read_json('../output/data/mongo.json')
    pv = df['id'].groupby(df['deviceId']).count().count()
    print(pv)


# my_test.remote()


def my_test_modin():
    mdf = mpd.read_json('../output/data/mongo.json')
    pv = mdf['id'].groupby(mdf['deviceId']).count().count()
    print(pv)


# start = time.time()
# object_id = my_test()
# print(object_id)
# end = time.time()
# print('Runned %d s' % (end - start))


start = time.time()
object_id = my_test.remote()
print(ray.get(object_id))
end = time.time()
print('Runned by modin %d s' % (end - start))
