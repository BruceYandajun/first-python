import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-08-06"
# 生成的文件
file_name = "../output/user_operation.csv"
# 每日的数据量(最大是5w用户量)
every_day_max_count = 10

# 用户的list
user_list = pd.read_json("../output/data/yinlian-user-demo.txt")
# 物料list
item_list = pd.read_json("../output/data/yinlian-item-demo.txt")

s = time.time()
day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    day_start = random.randint(0, every_day_max_count // 2)
    day_end = random.randint(every_day_max_count // 2, every_day_max_count)
    for i in range(day_start, day_end):
        data = {
            "startTimestamp": [startTimestamp],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77".format(i)],
            "bannerShowsNum": [random.randint(0, 5)]
        }
        df = df.append(pd.DataFrame(data), ignore_index=True)
        if first:
            df.to_csv(file_name, header=True, index=False, mode="w")
            df = pd.DataFrame()
        first = False
    if not first:
        df.to_csv(file_name, header=False, index=False, mode="a")
    print("Day {0}  {1} done ----!".format(day, startTimestamp))

e = time.time()
print('Runned %d s' % (e - s))
