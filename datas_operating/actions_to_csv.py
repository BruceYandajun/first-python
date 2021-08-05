import random
import pandas as pd
from pandas import DataFrame
import time

# 开始日期
start = "2021-07-01"
# 结束日期
end = "2021-07-31"
# 生成的文件
file_name = "user_operation.csv"
# 每日的数据量
every_day_count = 50000

day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = DataFrame()
    for i in range(0, every_day_count):
        data = {
            "startTimestamp": [day],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77".format(i)],
            "bannerShowsNum": [random.randint(0, 5)]
        }
        df = df.append(DataFrame(data), ignore_index=True)
        if first:
            df.to_csv(file_name, header=True, index=False, mode="w")
            df = DataFrame()
        first = False
    if not first:
        df.to_csv(file_name, header=False, index=False, mode="a")
    print("Day {0}  {1} done ----!".format(day, startTimestamp))

