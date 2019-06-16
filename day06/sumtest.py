
import random
import numpy
# 定义类，用于求和，传两个参数用于表示求和范围，申明方法有全部求和，有奇数，有偶数,每一个方法里有两种实现方式
class SumTest():
    sum1 = 0
    def __init__(self,para0,para1):
        self.para0 = para0
        self.para1 = para1
    # 实现两个数之间的总和
    def sum_all(self):
        self.sum1 = 0
        for i in range(self.para0,self.para1+1):
            self.sum1 += i
        print(self.sum1)
        print(sum(range(self.para0, self.para1+1)))
    # 实现两个数之间奇数的和
    def sum_odd(self):
        self.sum1 = 0
        if self.para0 % 2 == 0:
            for i in range(self.para0+1,self.para1+1,2):
                self.sum1 += i
            print(self.sum1)
            print(sum(range(self.para0+1, self.para1 + 1, 2)))
        else:
            for i in range(self.para0,self.para1+1,2):
                self.sum1 += i
            print(self.sum1)
            print(sum(range(self.para0,self.para1+1,2)))
    # 实现两个数之间偶数的和
    def sum_even(self):
        self.sum1 = 0
        if self.para0 % 2 == 0:
            for i in range(self.para0,self.para1+1,2):
                self.sum1 += i
            print(self.sum1)
            print(sum(range(self.para0,self.para1+1,2)))
        else:
            for i in range(self.para0+1,self.para1+1,2):
                self.sum1 += i
            print(self.sum1)
            print(sum(range(self.para0+1,self.para1+1,2)))



# 递归求和
def test_sum(num):
    if num >=1:
        res = num +test_sum(num-1)
    else:
        res = 0
    return res

if __name__ == '__main__':

    pass
