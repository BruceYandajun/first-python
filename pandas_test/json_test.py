import pandas as pd

df = pd.read_json('../output/data/sites.json')
print(df)
df.to_csv("../output/sites.csv")
oth = pd.DataFrame({
    'id': [10, 11],
    'name': ['a', 'b'],
    'url': ['http', 'www']
})
new_df = df.append(other=oth, ignore_index=True)
print(new_df)
new_df.to_json('../output/data/sites_new.json')
