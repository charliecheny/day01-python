from functools import reduce
# 冒泡排序一普通
def buffersort(list1):
    # 外循环控制循环趟数
    for i in range(len(list1)-1):
        # 内循环控制每趟的比较次数
        for j in range(len(list1)-i-1):
            # 比较大小并交换位置
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
# 冒泡排序二优化 定义变量控制循环趟数，一旦发现循环中不进行交换了就停止循环
def buffersort2(list1):
    for i in range(len(list1)-1):
        # 定义变量为假值
        flag = False
        for j in range(len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                # 如果交换了，则令flag为真
                flag = True
        if not flag:
            break
    return list1
# 冒泡排序三优化 搅拌排序/鸡尾酒排序 （处理最大值在两边的极端情况，写成双向排序提交效率
def buffersort3(list1):
    for i in range(len(list1) - 1):
        # 定义变量控制循环
        flag = False
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                # 左右交换
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                flag = True
        # 一趟循环结束，有交换则使循环再从右到左进行排序
        if flag:
            flag = False
            # 从倒数第二个开始比较
            for j in range(len(list1) - 2 - i, 0, -1):
                if list1[j - 1] > list1[j]:
                    list1[j], list1[j - 1] = list1[j - 1], list1[j]
                    flag = True
        # 一趟循环结束，没有进行交换则退出循环
        if not flag:
            break
    return list1
# 冒泡排序四，可以自定义传入函数比较字符串、或类的大小
def buffersort4(list1, comp = lambda x, y: x > y):
    # 第一次循环控制循环趟数
    for i in range(len(list1)-1):
        # 定义变量控制循环的停止
        flag = False
        for j in range(len(list1)-1-i):
            if comp(list1[j], list1[j+1]):
                list1[j], list1[j+1] = list1[j+1], list1[j]
                flag = True
        if flag:
            flag = False
            for j in range(len(list1)-2-i,0,-1):
                if comp(list1[j-1],list1[j]):
                    list1[j-1], list1[j] = list1[j], list1[j-1]
        if not flag:
            break

    return list1
# list1 = ['dog','act','abc','sheep','boolean','true']
# # 先进行了字母顺序排序，再进行了长度大小排序
# print(buffersort4(list1, lambda a, b: a > b))
# print(buffersort4(list1, lambda a, b: len(a) > len(b)))
if __name__ == '__main__':
    list1 = [44, 25, 17, 12, 65, 23, 32, 53]
    cal = reduce(lambda x, y:x * y,[1,2,3,4,5],4)
    print(cal)
    pass