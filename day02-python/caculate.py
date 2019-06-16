import random
import operator
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

class Demo():
    def calculate(self,blist):
        sum = 0
        for i in range(len(blist)):
            blist[i] += 1
            sum += blist[i]
        return sum

    def random_demo(self):
        list1 = []
        while len(list1)<10:
            list1.append(random.randint(0,100))
        list1.sort()
        print(list1[0:3])
        return list1

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            newNum = 0
            for i in str(num):
                newNum += int(i)
            num = newNum
        return num

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1
    # 实现1000以内的3的倍数
    def demo2(self):
        list = []
        for i in range(1,1001):
            if i%3 == 0:
                list.append(i)
            else:
                continue
        print(list)




if __name__ == '__main__':
    # math_operator(8,3)
    # comp_operator(8,3)
    # 列表解析实现1000以内的3的倍数
    # list1 = [i for i in range(1, 1001) if i % 3 == 0]
    # blist = [1,2,3,4]
    # demo = Demo()
    # print(demo.addDigits2(125))
    # print(demo.random_demo())
    # demo.calculate(blist)
    # print(demo.calculate(blist))
    # print(blist)
    pass