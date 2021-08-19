import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-08-20"
# 生成的文件
file_name = "../output/yinlian/item_operation_daily_stats.csv"
# 单位数据量级
amount_unit = 100

# 物料的list
item_list = pd.read_json("../input/yinlian/item_info.json", lines=True)["_id"]
item_count = item_list.count()

channel_list = ["FOLLOW", "REC", "VIDEO", "DIGITAL", "FINANCE", "TOURISM", "FOOD", "AUTOMOBILE", "VARITY", "RELATED", "SEARCH", "HOT_SEARCH", "AUTHOR_PAGE", "SUBJECT_PAGE"]


s = time.time()
day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    day_start = random.randint(0, item_count // 2)
    day_end = random.randint(item_count // 2 + 1, item_count - 1)
    for i in range(day_start, day_end):
        data = {
            "_class": ["com.baidu.acg.imt.puka.manage.entity.ItemOperationDailyStatsEntity"],
            "startTimestamp": [startTimestamp],
            "createTime": [startTimestamp],
            "updateTime": [startTimestamp],
            "itemId": [item_list[i]],
            "channel": [random.choice(channel_list)],
            "sharingNum": [random.randint(0, 5 * amount_unit)],
            "clickNums": [random.randint(0, 5 * amount_unit)],
            "likesNum": [random.randint(2, 5 * amount_unit)],
            "cancelLikesNum": [random.randint(0, 1 * amount_unit)],
            "showsNum": [random.randint(5, 10 * amount_unit)],
            "clicksNum": [random.randint(0, 5 * amount_unit)]
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
