import pandas as pd

a = [1, 2, 3]
mySeries = pd.Series(a)
print(mySeries)

a = ["Google", "Runoob", "Baidu"]
mySeries = pd.Series(a, index=['x', 'y', 'z'])
print(mySeries['x'])

sites = {1: 'Google', 2: 'Runoob', 3: 'Baidu'}
mySeries = pd.Series(sites)
print(mySeries)
