# 内循环
def list_bianli():
    for i in range(5):
        print('hello world')
        for j in range(2):
            print('内循环')
# 九九乘法表正序
def chengfabiao1():
    for i in range(1,10):
        for j in range(1,i+1):
            # 2为了对齐，代表s最小为两位宽度，s代表占位符，%代表格式化，后面跟格式形式  print默认参数为end='\n',所以会换行
            print('%2s * %2s = %2s' %(j,i,i*j),end = ' ')
        print(' ')
#九九乘法表倒序
def chengfabiao2():
    for i in range(9,0,-1):
        for j in range(1,i+1):
            print('%s * %s = %s' % (i, j, i * j), end=' ')
        print(' ')
# 输出两个数中的最大值
def if_demo(a,b):
    if a > b:
        print(a)
    else :
        print(b)
# 求1-50的奇数的和
def sum_jishu():
    sum = 0
    for i in range(1,51,2):
        sum += i
    print(sum)
def sum_jishu2():
    sum = 0
    for i in range(50):
        if i % 2 == 0:
            i = i +1
            sum += i
        else:
            continue
    print(sum)
# 求两个参数之间偶数的和，两个参数都包含
def sum_test1(aint,bint):
    if aint<bint :
        a = aint
        b = bint
    else:
        a = bint
        b = aint
    sum = 0
    if a % 2 == 0:
        if b % 2 == 0:
            for i in range(a, b + 1, 2):
                sum = sum + i
        else:
            for i in range(a, b, 2):
                sum = sum + i
    else:
        if b % 2 == 0:
            for i in range(a + 1, b + 1, 2):
                sum = sum + i
        else:
            for i in range(a + 1, b, 2):
                sum = sum + i
    print(sum)
# 方法二 求两个参数之间偶数的和，两个参数都包含
def sum_test2(aint,bint):
    a = aint if aint < bint else bint
    b = bint if aint < bint else aint
    sum = 0
    for i in range(a,b+1):
        if i%2 == 0:
            sum = sum + i
        else:
            continue
    print(sum)
# 求两个参数之间偶数的和，两个参数不包含的
def sum_test3(aint,bint):
    if aint<bint :
        a = aint
        b = bint
    else:
        a = bint
        b = aint
    sum = 0
    if a % 2 == 0:
            for i in range(a+2, b, 2):
                sum = sum + i
    else:
            for i in range(a + 1, b , 2):
                sum = sum + i
    print(sum)
# 方法二 求两个参数之间偶数的和，两个参数不包含的
def sum_test4(aint,bint):
    # 三元表达式优化：a = A if boolean else B boolean为真则a=A 为假则a=B
    a = aint if aint <= bint else bint
    b = bint if aint < bint else aint
    sum = 0
    for i in range(a+1,b):
        if i%2 == 0:
            sum = sum + i
        else:
            continue
    print(sum)

if __name__ == '__main__':
    sum_test4(10,10)
