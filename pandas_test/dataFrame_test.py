import pandas as pd

# data = [['Google', 10], ['Baidu', 20]]
# df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=int)
# print(df)
#
# print()
# data = {'Site': ['Google', 'Baidu', 'Facebook'], 'Age': [10, 20, 15]}
# df = pd.DataFrame(data, index=['x', 'x', 'y'])
# df = df.groupby(level=0).agg(s=("Age", "sum"))
# print(df)
#
# print()
# data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20, 'd': 50}]
# df = pd.DataFrame(data)
# print(df)
#
# # get count(*) from dataframe, reference:
# # https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
# # slowest
# print(len(df.index))
# print(df.shape[0])
# # fasted
# print(df[df.columns[0]].count())
#
# df = pd.read_json("../input/data.json", lines=True)
# print(df)
# df = df[["score", "name"]]
# print(df)
# print(type(df))
# d = df.to_dict(orient="records")
# print(type(d))
# print(d)
#
# df1 = pd.DataFrame([{"pv": 1}], index=["2021-11-11", "2021-11-12"])
# df2 = pd.DataFrame([{"uv": 3}, {"uv": 4}], index=["2021-11-12", "2021-11-13"])
# print(df1.join(df2))
# print(df1.merge(df2, left_index=True, right_index=True))
# print(pd.concat([df1, df2], axis=1))
#
#
# df1 = pd.DataFrame.from_dict(
#     {
#         "2021-11-11": {
#             "pv": 1
#         },
#         "2021-11-12": {
#             "pv": 1
#         }
#     }, orient="index")
# df2 = pd.DataFrame.from_dict(
#     {
#         "2021-11-12": {
#             "uv": 3,
#             "pv": 6
#         },
#         "2021-11-13": {
#             "uv": 4
#         }
#     }, orient="index")
#
# df3 = pd.DataFrame.from_dict(None)
# print(pd.concat([df1, df2, df3], axis=0).groupby(level=0).sum())
# print(df1.append(df2).groupby(level=0).sum())

data1 = {
    "day": ["2022-11-11", "2022-11-12", "2022-11-12", "2022-11-12", "2022-11-13"],
    "device_id": ["a", "b", "c", "b", "d"],
    "entry": ["APP", "APP", "FOOD", "APP", "FOOD"]
}
df1 = pd.DataFrame(data1)
df1 = df1.groupby(["day", "entry"]).agg(
    pv=("device_id", "count")
)
print(df1.groupby(df1.index.names).sum())

data2 = {
    ("2022-11-11", "APP"): {
        "uv": 2
    },
    ("2022-11-12", "APP"): {
        "uv": 3
    }
}
df2 = pd.DataFrame.from_dict(data2, orient="index")
df2.index.names = df1.index.names
print(f"------------------------\n{df2}")
print(pd.concat([df1, df2], axis=0).groupby(df1.index.names).sum())
