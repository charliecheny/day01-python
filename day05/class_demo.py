# class 类

def jiujiu():
    for x in range(1,10):
        for y in range(1,x+1):
            # print默认以end='\n'结束,所以都会换行
            print('%2s * %2s = %2s'%(y,x,x*y),end=' ')
        print(' ')
if __name__ == '__main__':
    jiujiu()


class Human(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.sex = sex
        self.age = age

    def myInfo(self):
        print('我叫%s, 今年%s岁, %s'%(self.name, self.age, self.sex))

class Female(Human):

    def myInfo(self):
            print('我今年%s岁' % ( self.age))