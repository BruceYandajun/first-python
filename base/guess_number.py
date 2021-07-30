number = 7
guess = -1
while guess != number:
    guess = int(input("请输入数字:"))
    if guess == number:
        print("恭喜你，猜对了!!!")
    elif guess > number:
        print("你猜的太大了")
    else:
        print("你猜的太小了")
