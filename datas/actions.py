import random

from pandas import DataFrame

data = {
    'startTimestamp': [1620748800000, 1620835200000],
    'deviceId': ['1_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77', '2_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77'],
    'bannerShowsNum': [10, 5]
}
df = DataFrame(data)

a = random.randint(0, 5)
print(a)

for i in range(0, 5):
    print(i)

print()
json = df.to_json(orient='records')
print(json)
