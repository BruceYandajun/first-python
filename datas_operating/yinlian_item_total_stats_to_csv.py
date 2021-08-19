import random
import pandas as pd
import time

# 生成的文件
file_name = "../output/yinlian/item_total_stats.csv"
# 单位数据量级
amount_unit = 100

# 物料的list
item_list = pd.read_json("../input/yinlian/item_info.json", lines=True)["_id"]
item_count = item_list.count()

s = time.time()

first = True
startTimestamp = round(time.time() * 1000)
df = pd.DataFrame()
for i in range(0, item_count):
    data = {
        "endTimestamp": [startTimestamp],
        "createTime": [startTimestamp],
        "updateTime": [startTimestamp],
        "itemId": [item_list[i]],
        "clicksNum": [random.randint(0, 5)],
        "showsNum": [random.randint(0, 5)],
        "likesNum": [random.randint(0, 5)],
        "sharingNum": [random.randint(0, 5)],
        "cancelLikesNum": [0],
        "ctr": [0.1]
    }
    df = df.append(pd.DataFrame(data), ignore_index=True)
    if first:
        df.to_csv(file_name, header=True, index=False, mode="w")
        df = pd.DataFrame()
    first = False
if not first:
    df.to_csv(file_name, header=False, index=False, mode="a")

e = time.time()
print('Ran %d s' % (e - s))
