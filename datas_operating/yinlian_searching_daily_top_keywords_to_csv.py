import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-09-17"
# 生成的文件
file_name = "../output/yinlian/searching_daily_top_keywords.csv"
# 单位数据量级
amount_unit = 1

keywords = ["暴雨", "百度", "中秋节", "AI智能", "自动驾驶", "塔利班", "阿富汗", "奥运会"]

s = time.time()
day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    for i in range(0, random.randint(100 * amount_unit, 200 * amount_unit)):
        data = {
            "startTimestamp": [startTimestamp],
            "createTime": [startTimestamp],
            "keyword": [random.choice(keywords)],
            "searchNum": [random.randint(0, 5)]
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
