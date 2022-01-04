import time

import pandas as pd

f = "actions_500w.csv"
dfs = []
for i in range(0, 2):
    if ".pkl" in f:
        dfs.append(pd.read_pickle(f))
    elif ".csv" in f:
        dfs.append(pd.read_csv(f))
    else:
        print("file error!")
total_df = pd.DataFrame()
start = time.time()
for df in dfs:
    total_df = total_df.append(df, ignore_index=True)
end = time.time()
print(f"Append {f} {len(dfs)} times cost {end - start} s")
print(total_df["nid"].size)
