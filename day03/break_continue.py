
def continue_demo():
    for i in range(5):
        print('第%s次循环'%i)
        if i == 2:
            print(' ')
            continue
        print('第%s次循环，if判断后'%i)
        print(' ')
def open_demo():
    text_io = open('test.text','r')
    readline = text_io.readline(2)
    print(readline)
    readlines = text_io.readlines()
    print(readlines)

if __name__ == '__main__':
    open_demo()
    pass