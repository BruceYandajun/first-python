from datetime import datetime, timedelta
from string import Template
import pandas as pd


def generate_range_hours(start, end, file_path):
    hour_time_list = pd.date_range(start, end, freq="H").tz_localize("UTC")
    for h in hour_time_list:
        print(generate_file_path(h.strftime('%Y-%m-%d %H'), file_path))


# 2021-10-12 00
def generate_file_path(date_hour, file_path):
    a = date_hour.split(" ")
    temp_dict = {"split_day": a[0], "split_hour": a[1]}
    temp = Template(file_path)
    new_file_path = temp.substitute(temp_dict)
    return new_file_path


file_p = "/data/actions/${split_day}/actions_${split_hour}.csv"
start_timestamp = 1635696000000 // 1000
end_timestamp = 1635782400000 // 1000

generate_range_hours(datetime.fromtimestamp(start_timestamp).strftime('%Y-%m-%d %H'),
                     datetime.fromtimestamp(end_timestamp).strftime('%Y-%m-%d %H'), file_p)

# last 30 day ago
print("---------------------------")
generate_range_hours((datetime.now() - timedelta(hours=30)).strftime('%Y-%m-%d %H'),
                     datetime.now().strftime('%Y-%m-%d %H'), file_p)
