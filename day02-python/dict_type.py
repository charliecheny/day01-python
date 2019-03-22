
import json

# 声明一个全量 dict 变量 (字典)
adict = {"name":"charlie","pwd":"123456"}
# 这是一个字符串，不过它是json格式，也是字典的格式
adictStr = '{"name":"charlie","pwd":"123456数字"}'

if __name__ == '__main__':
    # print(adict['name'])
    # adict.pop('name')
    # print(adict)
    print(type(adictStr))
    dump = json.loads(adictStr)
    print(type(dump))
    print(dump)
    str1 = json.dumps(dump,ensure_ascii=False)
    print(type(str1))
    print(str1)