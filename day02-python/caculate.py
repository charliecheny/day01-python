
# 数学运算符
def math_operator(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
# 比较运算符
def comp_operator(a,b):
    print(a > b)
    print(a < b)
    print(a == b)
    print(a >= b)
    print(a != b)




if __name__ == '__main__':
    # math_operator(8,3)
    # comp_operator(8,3)
    # 实现1000以内的3的倍数
    list = []
    for i in range(1,1001):
        if i%3 == 0:
            list.append(i)
        else:
            continue
    print(list)
    # 列表解析实现1000以内的3的倍数
    list1 = [i for i in range(1,1001) if i % 3 == 0]
    print(list1)