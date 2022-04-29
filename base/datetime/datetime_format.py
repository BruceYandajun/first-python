from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
pre = now - timedelta(days=7)
print(pre)


dt = datetime.fromtimestamp(datetime.now().timestamp())
print(dt.strftime("%Y-%m-%d"))


print(1632704172361 // 1000)
