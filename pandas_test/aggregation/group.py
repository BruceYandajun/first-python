from pandas import DataFrame
import numpy as np

df = DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randn(5),
    'data2': np.random.randn(5)
})
print(df)
# 选取data1的数据列按照key1进行分组，求平均值
grouped = df['data1'].groupby(df['key1']).mean()
print(grouped)

# 选取data1的数据列按照key1，key1进行分组，求平均值
grouped = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(grouped)

# size方法得到分组的大小
grouped = df.groupby([df['key1'], df['key2']]).size()
print(grouped)

# count方法得到分组后其它字段的个数
grouped = df.groupby([df['key1'], df['key2']]).count()
print(grouped)

# 对分组进行迭代
for name, group in df.groupby(df['key1']):
    print(name)
    print(group)

# 将分组的结果装成一个字典
pieces = dict(list(df.groupby('key1')))
print(pieces)
print(pieces['a'])
print(pieces['b'])

# 选择分类数据中的一个或一组
result1 = df.groupby(['key1', 'key2'])[['data2']].mean()
print(result1)
print(type(result1))
result2 = df['data2'].groupby([df['key1'], df['key2']]).mean()
print(result2)
print(type(result2))
