import os
import pandas as pd
print(os.path.exists("/data/government/das/data/2022030101/actions.csv"))
print(os.path.exists("http://10.137.16.163:8811/data/government/das/data/2022030101/actions.csv"))
df = pd.read_csv("http://10.137.16.163:8811/data/government/das/data/2022030101/actions.csv")
print(df)
