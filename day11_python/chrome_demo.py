from selenium import webdriver
import requests
import os
from Common import baseui
from Testcase import conftest
if __name__ == '__main__':
    chrome = webdriver.Chrome(os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe"))
    # chrome.get("https://www.baidu.com/")
    # chrome.find_element_by_id("kw").send_keys('徐挥豪')
    # chrome.find_element_by_id("su").click()
    # chrome.find_element_by_xpath("//input[@id='kw']").send_keys('徐挥豪')
    # chrome.find_element_by_xpath("//input[@id='su']").click()
    # chrome.find_element_by_name("wd").send_keys("徐挥豪")
    # chrome.find_element_by_class_name("s_ipt").send_keys("徐挥豪")
    baseui = baseui.baseUI(chrome)
    chrome.get("https://www.baidu.com")
    baseui.send_keys('diyibu','//input[@id="kw"]','xuhuihao')
    chrome.close()
    # browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__),"../chromedriver/chromedriver.exe"))
    # browser.get("http://www.51testing.com/zhuanti/selenium.html")
