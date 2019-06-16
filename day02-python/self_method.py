import random
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
# 给一个列表和目标值，找出列表中任意三个数相加等于目标值的三个数
def solution(nums,target):
    list2 = []
    for i in range(0, len(nums) - 2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    list = []
                    list.append(nums[i])
                    list.append(nums[j])
                    list.append(nums[k])
                    list.sort()
                    list2.append(list)
    print(list2)
    # 去重
    for i in list2:
        while list2.count(i) > 1:
            del list2[list2.index(i)]
    print(list2)
# 给一个列表和目标值，找出列表中任意二个数相加等于目标值的二个数的索引
def solution2(nums,target):
    list2 = []
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j]  == target:
                 list = []
                 list.append(i)
                 list.append(j)
                 list.sort()
                 list2.append(list)
    print(list2)


# 打印出100以内所有的勾股数
def gougu():
    for i in range(1,100):
        for j in range(i+1,100):
            for k in range(j+1,100):
                if i*i + j*j == k*k:
                    print(i,j,k)

# 更相减陨术  求出两个数a,b的最大公约数 : 用递归做
def gongyue(a,b):
    if a > b:
        a = a - b
    else:
        b = b - a
    if a == b:
        return a
    else:
        return gongyue(a,b)

 # 简单的生成器函数
def my_gen():
     n=1
     print("first")
     # yield区域
     yield n

     n+=1
     print("second")
     yield n

     n+=1
     print("third")
     yield n
if __name__ == '__main__':
    # l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    # l2 = list(set(l1))
    # l2.sort(key=l1.index)
    solution2([2,7,8,12],9)
    # print(l2)
    # list =(1, 3, 2, 6, 7, 9, 0, 4, 7, 5)
    # solution(list,10)
    # print(gongyue(27,18))

    # list = [4,3,6,8,2,12,5,9]
    # print(max(enumerate(list),key=lambda x : x[1]))
    # for i in list2:
    #     print(i)
    # print(enumerate(list))
    # print(list.index(max(list)), max(list))
