import random
import pandas as pd
import time

# 开始日期
start = "2021-08-01"
# 结束日期
end = "2021-08-20"
# 生成的文件
file_name = "../output/yinlian/product_operation_daily_stats.csv"
# 单位数据量级
amount_unit = 100

# 商品的list
product_list = pd.read_json("../input/yinlian/product_info.json", lines=True)["_id"]
product_count = product_list.count()

s = time.time()
day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
first = True
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = pd.DataFrame()
    day_start = random.randint(0, product_count // 2)
    day_end = random.randint(product_count // 2 + 1, product_count - 1)
    for i in range(day_start, day_end):
        data = {
            "bizTime": [startTimestamp],
            "createTime": [startTimestamp],
            "productId": [product_list[i]],
            "clickNums": [random.randint(0, 5 * amount_unit)],
            "showNums": [random.randint(0, 5 * amount_unit)]
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
