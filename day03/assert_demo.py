

if __name__ == '__main__':
    a = '12345678'
    # try except 异常判断；assert断言
    try:
        assert '5' in a
    except:
        print('0 not in a')
    print('-----------')