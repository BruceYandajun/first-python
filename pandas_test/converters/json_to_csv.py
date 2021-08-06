import pandas as pd

df = pd.read_csv("../../output/user_operation.csv")
print(df)
df.to_json("../../output/user_operation.json", orient="records", lines=True)
