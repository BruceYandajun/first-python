import pandas as pd

set1 = {1}
set2 = {2}
print(type(set1))
a = [1, 2, 2, 3]
mySeries = pd.Series(a)
print(mySeries.nunique())

a = ["Google", "Runoob", "Baidu"]
mySeries = pd.Series(a, index=['x', 'y', 'z'])
print(mySeries['x'])

sites = {1: 'Google', 2: 'Runoob', 3: 'Baidu'}
mySeries = pd.Series(sites)
print(mySeries)
