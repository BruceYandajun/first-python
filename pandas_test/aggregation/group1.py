import numpy as np
from pandas import DataFrame

people = DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
print(people)

# 添加几个NA值
people.loc[2:3, ['b', 'c']] = np.nan
print(people)

# 创建一个字典，根据列进行分组计算
mappings = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f': 'orange'}
by_column = people.groupby(mappings, axis=1)
print(by_column.sum())
