
# 普通写法
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
# 递归写法 ：调用函数自身、设置正确的返回值
def factorial_demo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_demo(n-1)
# 斐波那契数列 （兔子繁殖问题）
# 迭代写法(效率很高)
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('输入有误！')
        return -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
# 递归写法(递归比较好理解，效率低)
def fab_demo(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
# 汉诺塔
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)# 将前n-1个盘子从x移动到y上
        print(x,'-->',z) # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)# 将y上的n-1个盘子移动到z上

if __name__ == '__main__':
    # 用户输入调用方法
    # number = int(input('请输入一个正整数：'))
    # result = factorial_demo(number)
    # print('%d 的阶乘是:%d'%(number, result))
    # n个月后兔子诞生
    print(fab_demo(12))
