from pandas import DataFrame

df = DataFrame(data={'books': ['bk1', 'bk1', 'bk1', 'bk2', 'bk2', 'bk3'], 'price': [12, 12, 12, 15, 15, 17]})
print(df)
# 将books作为行索引
grouped = df.groupby('books', as_index=True).sum()
print(grouped)
print(type(grouped))
print(grouped['price'])

