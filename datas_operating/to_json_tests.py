from pandas import DataFrame

data = {
    'startTimestamp': [1620748800000, 1620835200000],
    'deviceId': ['1_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77', '2_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77'],
    'bannerShowsNum': [10, 5]
}

df = DataFrame(data)
# 默认展现，是按columns; lines如果设置为True，就是一行一行的json数据，不是标准json格式，首尾没有[]
path = "../output/data"
df.to_json(path + 'to_json_default.json')
df.to_json(path + 'to_json_columns.json', orient='columns')
df.to_json(path + 'to_json_index.json', orient='index')
df.to_json(path + 'to_json_records.json', orient='records', lines=True)
df.to_json(path + 'to_json_values.json', orient='values')
df.to_json(path + 'to_json_split.json', orient='split')
