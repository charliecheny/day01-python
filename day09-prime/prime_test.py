
import math
import time

prime = [2]
def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(3,int(math.sqrt(x)+1),2):
            if x % i == 0:
                return False
        return True

def prime_factorization(n):
    try:
        start = time.time()
        t_s = time.strftime('%H:%M:%S',time.localtime(time.time()))
        print('程序开始执行时间%s:'%t_s)
        for i in range(3,int(math.sqrt(n)+1),2):
            if is_prime(i):
                prime.append(i)
        for i in prime:
            if n % i == 0:
                print('%s=%s*%s'%(n,i,n//i))
        end = time.time()
        print('程序耗时:%ss'%round((end-start),2))
        return
    except:
        t_e=time.strftime('%H:%M:%S',time.localtime(time.time()))
        print('程序终止执行时间:%s'%t_e)

prime_factorization(7140229933)