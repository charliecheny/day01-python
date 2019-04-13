from Common import Assert
import random
from Common.baseui import *

class TestThirdDemo():
    def test_demo(self,driver):
        base = baseUI(driver)
        base.driver.get("http://192.168.60.132/#/login")
        base.click("登录","(//span[contains(text(),'登录')])[1]")
        base.click("点击营销","(//span[contains(text(),'营销')])[1]")
        base.click("点击优惠券列表","(//span[contains(text(),'优惠券列表')])[1]")
        base.click("点击编辑", "(//span[contains(text(),'编辑')])[1]")
        # 需要添加清空
        base.send_keys("修改金额","//label[contains(text(),'面额')]/following-sibling::div//input",3)
        base.click("点击提交", "//span[contains(text(),'提交')]")
        base.click("点击确定","//span[contains(text(),'确定')]")
        # 第一种
        # print(driver.page_source)
        # element = driver.find_element_by_xpath("//div[@role='alert']/p")
        # info = element.text
        # print(info)
        # print(type(info))
        # assertion = Assert.Assertions()
        # assertion.assert_in_text(info,"修改成功")
        # # time.sleep(2)
        # 第二种xpath
        element = driver.find_element_by_xpath('//div[@aria-label="提示"]/following-sibling::div/p[contains(text(),"修改成功")]')
        info = element.text
        assertion = Assert.Assertions()
        assertion.assert_in_text(info,"修改成功")