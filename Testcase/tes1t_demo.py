import pytest
import allure
from Common import Assert
from Common import Request
import requests
import json
# 声明Assert对象
assertions = Assert.Assertions()
# 申明Requset对象
request = Request.Request()
# 声明全局变量
myToken = ''
head2 = {'Authorization' : myToken}
list_data0 = []
url="http://192.168.60.125:8080"
# @allure.severity("critical")
# 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature("功能模块")
class TestShoppingTrolley(object):

    @allure.story("登录")
    # 给ids是为了给测试用例作区分，因为执行了三次，用户名都是错误的
    @pytest.mark.parametrize("pwd,name,msg",[("123456","admin","成功"),("223456","admin","错误"),("123456","admin2","错误")],
                             ids=['成功',"密码错误","用户名错误"])
    def test_login(self,pwd,name,msg):
        data = {"password": pwd, "username": name}
        post_request = request.post_request(url=url+"/admin/login", json=data)
        assertions.assert_code(post_request.status_code, 200)
        respJson = post_request.json()
        assertions.assert_in_text(respJson["message"],msg)
        respData = respJson['data']
        tokenBody = respData['token']
        tokenHead = respData['tokenHead']
        global myToken
        global head2
        myToken = tokenHead + tokenBody
        head2 = {'Authorization': myToken}
        get = request.get_request(url=url+'/admin/info', headers=head2)
        assertions.assert_code(get.status_code, 200)


    @allure.story("获取信息")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    def test_info(self):
        # global myToken
        # head2 = {'Authorization': myToken}
        get = request.get_request(url=url+'/admin/info', headers=head2)
        headers = get.request.headers
        print(headers)
        assertions.assert_code(get.status_code, 200)

    @allure.story("查看订单信息，显示5条数据")
    def test_list(self):
        # global myToken
        # head2 = {'Authorization': myToken}
        param1 = {'status': 1, 'pageNum': 1, 'pageSize': 5}
        get = request.get_request(url=url+'/order/list',params = param1, headers=head2)
        list_get = get.text
        print(list_get)
        assertions.assert_code(get.status_code, 200)
        global list_data0
        list_data0 = json.loads(list_get)['data']['list'][0]
        # list_data0 = json.loads(list_get)['data']['list'][1]

    @allure.story("订单发货")
    def  test_delivery(self):
        # global myToken
        # head2 = {'Authorization': myToken}
        global list_data0
        param1 = [{"deliveryCompany": "shunfengkaudi", "deliverySn": '', "orderId": list_data0['id']}]
        post = request.post_request(url=url+'/order/update/delivery',json = param1, headers=head2)
        delivery_res = post.json()
        print(delivery_res)
        assertions.assert_code(post.status_code, 200)

    @allure.story("关闭订单")
    def test_close(self):
        # global myToken
        # head2 = {'Authorization': myToken}
        global list_data0
        param1 = {"ids": list_data0['id'], 'note': 'guanbi'}
        post = request.post_request(url=url+'/order/update/close',params = param1, headers=head2)
        close_res = post.text
        print(close_res)
        assertions.assert_code(post.status_code, 200)

