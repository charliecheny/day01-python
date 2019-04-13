import requests
import json

def req_demo():
    # 请求登入接口
    json_body1 = {"username":"admin","password":"123456"}
    response1= requests.post(url='http://192.168.60.132:8080/admin/login',json=json_body1)
    login_res = response1.json()
    print(login_res)
    # 获取登录后的token
    tokenhead = login_res['data']['tokenHead']
    token = login_res['data']['token']
    head = {'Authorization':tokenhead + token}
    # info接口测试
    response2 = requests.get(url='http://192.168.60.132:8080/admin/info',headers = head)
    info_res = response2.text
    print(info_res)
    # list查看订单信息
    # 传参显示5条数据
    param1 = {'status':1,'pageNum':1,'pageSize':5}
    response3 = requests.get(url='http://192.168.60.132:8080/order/list',params = param1,headers = head)
    list_res = response3.text
    print(list_res)
    # list_res = response3.json()['data']['list']
    # for i in list_res:
    #     print(i)
    # 找一条未发货订单
    list_data0 = json.loads(list_res)['data']['list'][0]
    list_data1 = json.loads(list_res)['data']['list'][1]
    # delivery发货接口
    param2 = [{ "deliveryCompany": "shunfengkaudi", "deliverySn": '',"orderId":list_data0['id']},{"deliveryCompany": "shunfengkaudi", "deliverySn": '',"orderId":list_data1['id']}]
    response4 = requests.post(url='http://192.168.60.132:8080/order/update/delivery',json = param2,headers = head)
    delivery_res = response4.json()
    print(delivery_res)
    # close 关闭订单接口
    param3 = {"ids":[list_data0['id'],list_data1['id']],'note':'guanbi'}
    response5 = requests.post(url='http://192.168.60.132:8080/order/update/close',params = param3,headers = head)
    close_res = response5.text
    print(close_res)

    # print(requests.post(url='http://192.168.60.132:8080/admin/login', json={"username":"admin","password":"123456"}).content.decode('utf-8'))