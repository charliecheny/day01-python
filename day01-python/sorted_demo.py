alist = [4,2,8,3,6,1,7]
# for each in alist:
#     print (each)
#     alist.remove(each)
import requests
import operator

# 冒泡排序 优化版
def buffer_sort(list):
    for i in range(len(list)-1):
        flag = False
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flag = True
        if not flag:
            break
    return list
list2 = [(2,3,4),(3,5,2),(6,3,2),(9,2,5),(7,4,6)]
# 定义一个lambda，来取迭代器下标为1的数值
list3 = sorted(list2, key=lambda x: x[1], reverse=True)
print(list3)
student_tuples = [('Bob', 92),('Adam', 66),('Bart', 66),('Lisa', 88),]
# 使用operator模块的itemgetter方法，获取对象的第n个域的值，其实就是一个方法，和上面的lambda类似
student_tuples2 = sorted(student_tuples, key=operator.itemgetter(1), reverse=True)
print(student_tuples2)



if __name__ == '__main__':
    buffer_sort(alist)
    print(alist)
    sessions = requests.session()
    # 百度设置了反扒的话 可以加入user-agent
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    get = sessions.get('https://www.baidu.com',headers = head)
    # text = get.text
    encoding = get.encoding
    # print(text)
    print(encoding)
    requests.get('https://www.baidu.com')

