import pandas as pd

df = pd.read_json('sites.json')
print(df)
df.to_csv("sites.csv")

