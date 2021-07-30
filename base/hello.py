import keyword

print('hello world!')

a_ = 'abc'
print(a_)

# 注释
print(keyword.kwlist)

if True:
    print(1)
else:
    print(0)

myString = '123456789'

print(myString)  # 输出字符串
print(myString[0:-1])  # 输出第一个到倒数第二个的所有字符
print(myString[0])  # 输出字符串第一个字符
print(myString[2:5])  # 输出从第三个开始到第五个的字符
print(myString[2:])  # 输出从第三个开始后的所有字符
print(myString[1:7:2])  # 输出从第二个开始到第七个且每隔一个的字符（步长为2）
print(myString * 2)  # 输出字符串两次
print(myString + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

name = 'Bruce'
age = 30
print('%s is %d' % (name, age))
print('{0} is {1}'.format(name, age))

