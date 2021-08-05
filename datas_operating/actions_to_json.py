import random
import modin.pandas as pd
import time
import os

# 开始日期
start = "2021-07-01"
# 结束日期
end = "2021-07-31"
# 生成的文件
file_name = "../output/user_operation.csv"
# 每日的数据量
every_day_count = 50000
#
lines = False

os.remove(file_name)
print("Removed old files ----!")

day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    for i in range(0, 5):
        data = {
            "startTimestamp": [startTimestamp],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77".format(i)],
            "bannerShowsNum": [random.randint(0, 5)]
        }
        df = df.append(pd.DataFrame(data), ignore_index=True)
        df.to_json(file_name, orient="records", lines=lines)
    print("Day {0}  {1} done ----!".format(day, startTimestamp))

