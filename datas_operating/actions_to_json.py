import random
import pandas as pd
from pandas import DataFrame
import time
import os

start = "2021-07-01"
end = "2021-07-31"
file_name = "user_operation.json"
lines = False

os.remove(file_name)
print("Removed old files ----!")

day_list = pd.date_range(start=start, end=end).tz_localize("UTC")
for day in day_list:
    startTimestamp = int(time.mktime(day.timetuple()) * 1000)
    df = DataFrame()
    for i in range(0, 5):
        data = {
            "startTimestamp": [startTimestamp],
            "deviceId": ["{}_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77".format(i)],
            "bannerShowsNum": [random.randint(0, 5)]
        }
        df = df.append(DataFrame(data), ignore_index=True)
        df.to_json(file_name, orient="records", lines=lines)
    print("Day {0}  {1} done ----!".format(day, startTimestamp))

