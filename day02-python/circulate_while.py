# 练习一：逐一显示指定列表中的所有元素
def while1(l1):
    count = 0
    # 方法一
    while count < len(l1):
        print(l1[count])
        count +=1
    # 方法二
    while l1:
        print(l1[0])
        l1 = l1[1:]
    # 方法三
    while l1:
        print(l1[0])
        l1.pop(0)
# 练习二：求100以内的所有偶数之和
def while2():
    sum1 = 0
    i = 0
    while i < 100:
        sum1 += i
        i += 2
    else:
        print(sum1)
# 练习三：逐一显示指定字典的所有键，并于显示结束后说明总键数
def while3(d1):
    keylist = d1.keys()
    while keylist:
        print(keylist[0])
        keylist.pop(0)
    else:
        print(len(d1))
# 练习四：创建一个包含了100以内的所有奇数的列表
def while4():
    l1 = []
    x = 1
    while x < 100:
        l1.append(x)
        x += 2
    else:
        print(l1)
# 练习五：逆序逐一显示一个列表的所有元素
def while5(l1):
    while l1:
        print(l1.pop())
# 练习六：列表l1=[0,1,2,3,4,5,6],列表l2=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
# 以第一个列表中的元素为键，以第二个列表中元素为值生成字典d1;
def while6(l1,l2):
    d1 = {}
    count = 0
    if len(l1) == len(l2):
        while count < len(l1):
            # 直接给字典的键赋值就行，因为字典支持在原处修改
            d1[l1[count]] = l2[count]
            count += 1
        else:
            print(d1)
# 练习七：把用户输入的数据全部转换成字符装进列表中
def while7():
    test = []
    while True:
        x = input('Enter an entry:')
        if x == 'q' or x == 'quit':
            break
        else:
            test.append(x)
if __name__ == '__main__':
    pass