import pytest
import os
from selenium import webdriver
## 流程控制器，执行用例前都会先执行这个代码
@pytest.fixture(scope='session')
def driver():
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    # 打开浏览器
    dr = webdriver.Chrome(driver_path)
    dr.maximize_window()  # 最大化浏览器
    dr.set_page_load_timeout(10)#网页加载超时为10s
    dr.set_script_timeout(10)#js脚本运行超时10s
    dr.implicitly_wait(10)#元素查找超时时间10s
    yield dr
    dr.quit()

    # 隐式等待时间  等待页面元素全部加载完才行继续运行 implicitly_wait
    # 在使用隐式等待的时候，实际上浏览器会在你自己设定的时间内部断的刷新页面去寻找我们需要的元素
    # 它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位是，如果元素可以定位，则继续执行；
    # 如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。

    # 显示等待时间  等待直到元素出现才去操作，如果超时则报异常
    # WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
    # driver: 浏览器驱动
    # timeout: 最长超过时间，默认以秒为单位
    # poll_frequency: 监测的时间间隔，默认为0.5秒
    # ignored_exceptions: 超时后的异常信息，默认情况下抛NoSuchElementException异常
    # WebDriverWait一般有until和until_not方法配合使用