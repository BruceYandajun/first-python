import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-08-19"
# 生成的文件
out_file_name = "../output/yinlian/user_operation.csv"
# 每日的数据量(最大是5w用户量)
every_day_max_count = 10

# 用户的list
user_list = pd.read_json("../input/yinlian/yinlian-user-demo.txt", lines=True)["uid"]
user_count = user_list.count()
# user_count = 6
# 物料list
item_list = pd.read_json("../input/yinlian/yinlian-item-demo.txt", lines=True)["nid"]
item_count = item_list.count()
# 场景list
scene_codes = ["BANNER", "MINI_PROGRAM", "HOT_ACTIVITY", "PRODUCT_RECOMMEND", "BANK_APPLICATION"]
action_numbers = ["onlineNum", "recallNum", "showNum", "clickNum", "shareNum", "likeNum"]

s = time.time()
day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    day_start = random.randint(0, user_count // 2)
    day_end = random.randint(user_count // 2 + 1, user_count - 1)
    for i in range(day_start, day_end):
        data = {
            "startTimestamp": [startTimestamp],
            "uid": [user_list[i]],
            "ts": [startTimestamp],
            "nid": [random.choice(item_list)],
            "sceneCode": [random.choice(scene_codes)],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9".format(i)],
            "onlineNum": [random.randint(2000, 3000)],
            "recallNum": [random.randint(1000, 2000)],
            "showNum": [random.randint(500, 1000)],
            "clickNum": [random.randint(100, 200)],
            "shareNum": [random.randint(0, 100)],
            "likeNum": [random.randint(0, 100)]
        }
        df = df.append(pd.DataFrame(data), ignore_index=True)
        if first:
            df.to_csv(out_file_name, header=True, index=False, mode="w")
            df = pd.DataFrame()
        first = False
    if not first:
        df.to_csv(out_file_name, header=False, index=False, mode="a")
    print("Day {0}  {1} done ----!".format(day, startTimestamp))

e = time.time()
print('Ran %d s' % (e - s))
