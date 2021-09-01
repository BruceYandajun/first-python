import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-09-17"
# 生成的文件
file_name = "../output/user_operation_chunming.csv"
# 每日的数据量(最大是5w用户量)
every_day_max_count = 10

# 用户的list
user_list = pd.read_json("../output/data/yinlian-user-demo.txt", lines=True)["uid"]
user_count = user_list.count()
# user_count = 6
# 物料list
item_list = pd.read_json("../output/data/yinlian-item-demo.txt", lines=True)["nid"]
item_count = item_list.count()
# 事件list
action_types = ["REC", "ENTER", "EXIT", "CLICK", "PRODUCT_CLICK", "PRODUCT_SHOW", "BANNER_CLICK", "BANNER_SHOW", "SEARCH", "SHOW", "LIKE", "SHARE", "CANCEL_LIKE"]
action_numbers = ["recNum", "enterNum", "exitNum", "clicksNum", "productClicksNum", "productShowsNum", "bannerClicksNum", "bannerShowsNum", "searchNum", "showsNum", "likesNum", "sharingNum", "cancelLikesNum"]

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
            "nid": [item_list[random.randint(0, item_count - 1)]],
            "actionType": [action_types[random.randint(0, len(action_types) - 1)]],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9".format(i)],
            action_numbers[0]: [random.randint(0, 50)],
            action_numbers[1]: [random.randint(0, 50)],
            action_numbers[2]: [random.randint(0, 50)],
            action_numbers[3]: [random.randint(0, 50)],
            action_numbers[4]: [random.randint(0, 50)],
            action_numbers[5]: [random.randint(0, 50)],
            action_numbers[6]: [random.randint(0, 50)],
            action_numbers[7]: [random.randint(0, 50)],
            action_numbers[8]: [random.randint(0, 50)],
            action_numbers[9]: [random.randint(0, 50)],
            action_numbers[10]: [random.randint(0, 50)],
            action_numbers[11]: [random.randint(0, 50)],
            action_numbers[12]: [random.randint(0, 50)]
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


df = pd.read_csv(file_name)
df.to_json("../output/user_operation.json", orient="records", lines=True)
