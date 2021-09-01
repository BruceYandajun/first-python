import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-09-17"
# 生成的文件
file_name = "../output/yinlian/user_operation_daily_stats.csv"
# 单位数据量级
amount_unit = 1

s = time.time()
day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    for i in range(0, random.randint(100 * amount_unit, 200 * amount_unit)):
        data = {
            "startTimestamp": [startTimestamp],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77".format(i)],
            "uid": ["{}_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77".format(i)],
            "recNum": [random.randint(0, 5)],
            "enterNum": [random.randint(0, 5)],
            "exitNum": [random.randint(0, 5)],
            "clicksNum": [random.randint(0, 5)],
            "productClicksNum": [random.randint(0, 5)],
            "productShowsNum": [random.randint(0, 5)],
            "bannerClicksNum": [random.randint(0, 5)],
            "bannerShowsNum": [random.randint(0, 5)],
            "searchNum": [random.randint(0, 5)],
            "showsNum": [random.randint(0, 5)],
            "likesNum": [random.randint(0, 5)],
            "sharingNum": [random.randint(0, 5)],
            "cancelLikesNum": [random.randint(0, 5)],
            "stayDuration": [random.randint(0, 100*1000)],
            "enterDuration": [random.randint(0, 500*1000)]
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
print('Ran %d s' % (e - s))
