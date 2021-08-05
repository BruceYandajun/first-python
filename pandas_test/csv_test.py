import pandas as pd

df = pd.read_csv('../output/data/nba.csv')
print(df.head(5))
print(df.tail(5))
print(df.info())
