from selenium import webdriver

class TestFireFox:
    def test_demo1(self):
        browser = webdriver.Firefox(executable_path="geckodriver")
        browser.maximize_window()
        browser.get("https://www.baidu.com")
        browser.find_element_by_id("kw").send_keys("selenium")
        browser.find_element_by_id("su").click()
        browser.quit()