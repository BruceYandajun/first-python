import random
import pandas as pd
import time

user_list = pd.read_json("../output/data/yinlian-user-demo.txt", lines=True)
# print(user_list["uid"])
user_count = user_list["uid"].count()
print(user_count)
print(user_count / 2)
print(user_count // 2)
# print(type(user_list["uid"][5001]))
# print(user_list["uid"].count())


