import pandas as pd

data = [['Google', 10], ['Baidu', 20]]
df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=int)
print(df)

print()
data = {'Site': ['Google', 'Baidu'], 'Age': [10, 20]}
df = pd.DataFrame(data, index=['x', 'y'])
print(df)

print()
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20, 'd': 50}]
df = pd.DataFrame(data)
print(df)

# get count(*) from dataframe, reference:
# https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
# slowest
print(len(df.index))
print(df.shape[0])
# fasted
print(df[df.columns[0]].count())

df = pd.read_json("../input/data.json", lines=True)
print(df)
df = df[["score", "name"]]
print(df)
print(type(df))
d = df.to_dict(orient="records")
print(type(d))
print(d)
