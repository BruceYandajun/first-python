from datetime import datetime

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))


dt = datetime.fromtimestamp(1632704172361 // 1000)
print(dt.strftime("%Y-%m-%d"))


