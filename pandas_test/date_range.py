import pandas as pd
import time

time_list = pd.date_range(start="2021-07-01", periods=30).tz_localize("UTC")
print(time_list)
for i in time_list:
    print(int(time.mktime(i.timetuple()) * 1000))
