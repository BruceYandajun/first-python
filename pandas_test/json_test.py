import pandas as pd

df = pd.read_json('sites.json')
print(df)
df.to_csv("sites.csv")
oth = pd.DataFrame({
    'id': [10, 11],
    'name': ['a', 'b'],
    'url': ['http', 'www']
})
new_df = df.append(other=oth)
print(new_df)
