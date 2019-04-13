import os
import time
from selenium import webdriver
from Common import Assert
from Testcase import conftest
class TestFirstUIDemo:
    def test_testdemo1(self,driver):
        # 打开浏览器
        # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # print(driver_path)
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        time.sleep(2)
        # 输入用户名
            # 先找到用户名的xpath
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='username']").click()
            # 清空文本框
        driver.find_element_by_xpath("//input[@name='username']").clear()
            # 输入内容
        driver.find_element_by_xpath("//input[@name='username']").send_keys('')
        time.sleep(2)
        # 输入密码
            # 找到密码xpath
        driver.find_element_by_xpath("//input[@name='password']").click()
        driver.find_element_by_xpath("//input[@name='password']").clear()
        time.sleep(2)
            # 输入密码
        driver.find_element_by_xpath("//input[@name='password']").send_keys('')
        # 定位到登录的按钮
        denglu = driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]")
        # 点击按钮
        denglu.click()
        time.sleep(2)
        # 断言
        assertion = Assert.Assertions()
        assertion.assert_in_text(driver.page_source,'首页')
        # 点击营销
        driver.find_element_by_xpath("//span[contains(text(),'营销')]").click()
        # 点击优惠券列表
        driver.find_element_by_xpath("//span[contains(text(),'优惠券列表')]").click()
        # 输入优惠券名称
        driver.find_element_by_xpath("//input[@placeholder='优惠券名称']").click()
        driver.find_element_by_xpath("//input[@placeholder='优惠券名称']").send_keys('全品类通用券')
        # 点击查询搜索
        driver.find_element_by_xpath("//span[contains(text(),'查询搜索')]").click()
        time.sleep(5)
        # assertion.assert_in_text(driver)
        driver.quit()