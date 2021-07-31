# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("这是文本！！")

# 读文本
with open("test.txt", "rt") as in_file:
    text = in_file.read()
print(text)
