from selenium import webdriver
import time
# # 打开浏览器  wd是浏览器的对象
# wd = webdriver.Chrome()
# # 打开网址
# wd.get('https://www.baidu.com')
# # 截图
# wd.save_screenshot('baidu,png')
# # 设置窗口大小
# wd.set_window_size(1280,800)
# # 输入搜索内容
# kw = wd.find_element_by_id('kw')
# # 输入的内容
# kw.send_keys('小姐姐')
# # 点击百度一下
# wd.find_element_by_id('su').click()
# # 休眠3秒钟
# time.sleep(3)
# # 关闭浏览器
# wd.quit()


'''
模拟登陆 qq 邮箱
'''
# 打开浏览器
wd = webdriver.Chrome(executable_path='C:\\Users\Charlie chen\PycharmProjects\myedu\chromedriver\chromedriver.exe')
# 隐式等待
wd.implicitly_wait(10)
# 打开邮箱网站
wd.get('https://mail.qq.com')
# 调整窗口大小
wd.maximize_window()
# 切换iframe
login_iframe = wd.find_element_by_id('login_frame')

wd.switch_to.frame(login_iframe)
# 点击账号密码登录
# wd.find_element_by_id('switcher_plogin').click()
wd.find_element_by_id('u').send_keys('1475323953')
wd.find_element_by_id('p').send_keys('weixiao-smile')
wd.find_element_by_id('login_button').click()
# 获取邮件
wd.find_element_by_id('readmailbtn_link').click()
email = wd.find_element_by_class_name('i M')
print(email)
wd.quit()