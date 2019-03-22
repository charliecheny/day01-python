# 声明全局变量
alist = ['this','is',2,5,3,'a','pig']
blist = [1,2,3,4,5,7,6,8,9]
# 切片
def list_test1(alist):
    # 打印索引0-2的元素
    print(alist[0:2])
    # 打印索引1-6的元素，步进值为2
    print(alist[1:6:2])

# 定义变量并打印
def int_demo():
    aint = 1
    # print(aint)
    # print(type(aint))
    return aint

# 定义删除方法
def pop_demo(alist):
    # pop()方法两个作用，第一个取出最后一位的值，第二个从列表中取出删除的值
    print(alist.pop())
    print(alist)

# 列表排序的方法
def orderBy_demo():
    sort_demo()
    reverse_demo()
    pass

# 正序方法
def sort_demo():
    blist.sort()
    print(blist)
    pass

# 倒序方法
def reverse_demo():
    blist.reverse()
    print(blist)
    pass

# 声明加法
def add(aint, bint):
    return aint + bint

# 声明减法，参数为a,b
def sub(a, b):
    return a - b

# 声明main方法 kkk
if __name__ == '__main__':
    alist.insert(4,'add')
    print(alist)

    # orderBy_demo()
    # pop_demo(alist)
    # print(alist[0:8:3])
    # print('hello,world')
    # 给alist排序
    # print(sorted(alist))
    # s = int_demo()
    # print(s)

    # 调用
    # list_test1(blist)
    # 调用加法add 传入参数1,2 返回加法得值
    # result = add(1, 2)
    # print(result)
    # # 调用加法add 传入参数60,52 返回减法的值
    # c = sub(60, 52)
    # print(c)
    # int_demo()
    # print('"hello world"')
    # print(x)
