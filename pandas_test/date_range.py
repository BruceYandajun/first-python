import pandas as pd
import time

time_list = pd.date_range(start="2021-07-01", end="2021-07-31").tz_localize("UTC")
print(time_list.size)
for i in time_list:
    print(int(time.mktime(i.timetuple()) * 1000))
