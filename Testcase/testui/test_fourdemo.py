from Common import Assert
from Common.baseui import *
import random
class TestFourDemo:
    def test_demo(self,driver):
        base = baseUI(driver)
# 打开浏览器网址
        driver.get("http://192.168.60.132/#/login")
# 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")
# 点击订单
        base.click("点击订单","//span[text()='订单']")
# 点击订单列表
        base.click("点击订单列表","//span[text()='订单列表']")
# 点击订单状态
        base.click("点击订单状态", "//label[contains(text(),'订单状态')]/following-sibling::div//input")
# 点击待发货
        base.click("点击待发货", "//span[contains(text(),'待发货')]")
# 点击查询搜索
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
# 取第一个元素订单发货 取出订单id
        base.click("点击订单发货", "(//span[text()='订单发货'])[3]")
        element = driver.find_element_by_xpath(
            "//*[@id='app']/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div")
        info = element.text
        print(info)
# 点击配送方式
        base.click("点击配送方式",'//input[@placeholder="请选择物流公司"]')
# 点击圆通快递
        base.click("点击圆通快递","//span[contains(text(),'圆通快递')]")
# 输入物流单号
        base.send_keys("输入物流单号","(//input)[2]",random.randint(22230000,22240000))
# 点击确定 提交
        base.click("点击确定","//span[text()='确定']")
# 点击提示中的确定
        base.click('点击确定',"//div[@aria-label='提示']//span[contains(text(),'确定')]")
# 取出发货成功做断言
        element2 = driver.find_element_by_xpath("//div[@role='alert']/p")
        info2 = element2.text
        assertion = Assert.Assertions()
        assertion.assert_in_text(info2,"发货成功")
# 查看取出的订单id的订单状态是否为已发货做断言
        base.send_keys("点击输入订单", "//label[contains(text(),'输入搜索')]/following-sibling::div//input",info)
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        element3 = driver.find_element_by_xpath("//span[text()='查看订单']/ancestor::td/parent::tr//div[contains(text(),'已发货')]")
        info3 = element3.text
        print(info3)
        assertion = Assert.Assertions()
        assertion.assert_in_text(info3, "已发货")


    def test_demo2(self,driver):
        base = baseUI(driver)
        # 打开网站
        driver.get("http://192.168.60.132/#/login")
        # 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")
        # 点击订单
        base.click("点击订单","//span[text()='订单']")
        # 点击订单列表
        base.click("点击订单列表","//span[text()='订单列表']")
        # 点击订单状态为待发货
        base.click("点击订单状态", "//label[contains(text(),'订单状态')]/following-sibling::div//input")
        base.click("点击待发货", "//span[contains(text(),'待发货')]")
        # 点击搜索查询
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        # 订单编号边上的输入框全选按钮
        base.click("点击全选","(//label[@role='checkbox'])[1]/span/span")
        # 点击下拉框
        base.click("点击批量操作下拉框","//input[@placeholder='批量操作']")
        # 点击批量发货
        base.click("点击批量发货","//span[text()='批量发货']")
        # 点击确定
        base.click("点击确定","(//span[contains(text(),'确定')])[1]")
        # 写一个循环，一个个点击物流公司和编号
        nums = driver.find_elements_by_xpath("//tbody/tr/td[6]/div/div")
        for i,n in enumerate(nums):
            n.click()
            base.click("选择快递","(//span[text()='圆通快递'])[10]")
            base.send_keys("物流单号","(//tbody/tr/td[7]/div/div/input)[%d]" % (i+1),random.randint(22230000,22240000))
        # rows = len(driver.find_elements_by_xpath("//tbody/tr/td[6]/div/div"))
        # for i in range(1,rows+1):
        #     base.click("选择物流公司","(//tbody/tr/td[6]/div/div)[{0}]".format(i))
        #     base.click("选择快递", "(//span[text()='圆通快递'])[10]")
        #     base.send_keys("物流单号","(//tbody/tr/td[7]/div/div/input)[{0}]".format(i),random.randint(22230000,22240000))
        # 点击确定
        base.click("点击确定","//span[text()='确定']")
        # 点击提示中的确定
        base.click('点击确定', "//div[@aria-label='提示']//span[contains(text(),'确定')]")
        # 取出发货成功做断言
        element2 = driver.find_element_by_xpath("//div[@role='alert']/p")
        info2 = element2.text
        assertion = Assert.Assertions()
        assertion.assert_in_text(info2, "发货成功")