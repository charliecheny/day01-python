import random
secret = random.randint(1,10)
print('------我爱python-------')
temp = input('不妨猜一下我心里现在想的是哪个数字:')
guess = int(temp)
while guess != secret:
    input('猜错咯！重新输入吧:')
    guess = int(temp)
    if guess == secret:
        print('我曹，你是我心里的蛔虫吗？！')
        print('哼，猜中了也没有奖励')
    else:
        if guess > secret:
            print('哥，大了大了~~')
        else:
            print('嘿，小了！小了！！')

print('游戏结束，不玩啦^_^')