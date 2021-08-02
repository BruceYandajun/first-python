from pandas import Series, DataFrame
import pandas as pd
import numpy as np

dict_obj = {
    'key1': ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'a'],
    'key2': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'data1': np.random.randint(1, 10, 8),
    'data2': np.random.randint(1, 10, 8)
}
df = DataFrame(dict_obj)
print(df)
# 按照key1分组求和
print('--------------------------------')
print(df.groupby('key1').sum())
# 将data1按key1分组求和
print('--------------------------------')
print(df['data1'].groupby(df['key1']).sum())
# 按照key1分组求最大值
print('--------------------------------')
print(df.groupby('key1').max())
# 将data1按key1分组求最大值
print('--------------------------------')
print(df['data1'].groupby(df['key1']).max())


# 自定义聚合函数，求分组中的最大值和最小值的差
def peak_range(df1):
    print(type(df1))
    return df1.max() - df1.min()


print(df.groupby('key1').agg(peak_range))

# 使用匿名函数
print(df.groupby('key1').agg(lambda df2: df2.max() - df2.min()))
# 使用多个聚合函数
print(df.groupby('key1').agg(['mean', 'std', 'count', peak_range]))
# 使用数据字典实现数据集的每一列使用不同的聚合函数
dict_mapping = {"data1": "mean", "data2": "sum"}
print(df.groupby('key1').agg(dict_mapping))


