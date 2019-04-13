
from Common import Assert
import random
from Common.baseui import *

class TestSecondUIDemo:
    def test_demo2(self,driver):
        base = baseUI(driver)
        # 打开网址
        base.driver.get("http://192.168.60.132/#/login")
        # 输入用户名
            # 先找到用户名的xpath
        # driver.find_element_by_xpath("//input[@name='username']").click()
        #     # 清空文本框
        # driver.find_element_by_xpath("//input[@name='username']").clear()
        #     # 输入内容
        # driver.find_element_by_xpath("//input[@name='username']").send_keys('')
        # time.sleep(2)
        # # 输入密码
        #     # 找到密码xpath
        # driver.find_element_by_xpath("//input[@name='password']").click()
        # driver.find_element_by_xpath("//input[@name='password']").clear()
        # time.sleep(2)
        #     # 输入密码
        # driver.find_element_by_xpath("//input[@name='password']").send_keys('')
        # 定位到登录的按钮
        # send_keys(driver,"(//span[contains(text(),'登录')])[1]",'')
        base.click('登录',"(//span[contains(text(),'登录')])[1]")
        # 断言
        assertion = Assert.Assertions()
        assertion.assert_in_text(driver.page_source,'首页')
        # 添加商品
            # 点击商品
        base.click("点击商品","(//span[contains(text(),'商品')])[1]")
            # 点击添加商品
        base.click("点击添加商品","(//span[contains(text(),'添加商品')])[1]")
            # 点击商品分类下拉框
        base.click("商品分类",'//span[@class="el-cascader__label"]')
            # 点击服装
        base.click("点击服装","//li[contains(text(),'服装')]")
            # 点击外套
        base.click("点击外套","//li[contains(text(),'外套')]")
            # 点击商品名称并输入charlie
        base.send_keys("点击商品名称","//label[contains(text(),'商品名称：')]/following-sibling::div//input",'charlie')
            # 点击副标题
        base.send_keys("点击副标题","//label[contains(text(),'副标题：')]/following-sibling::div//input",'chen')
            # 点击商品品牌
        base.click("点击商品品牌","//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        base.click("点击商品品牌","//span[contains(text(),'七匹狼')]")
            # 点击商品介绍
        base.send_keys("点击商品介绍","//label[contains(text(),'商品介绍：')]/following-sibling::div//textarea",'test')
            # 点击商品售价
        base.send_keys("点击商品售价","//label[contains(text(),'商品售价：')]/following-sibling::div//input",random.randint(80,90))
            # 点击市场价
        base.send_keys("点击市场价","//label[contains(text(),'市场价：')]/following-sibling::div//input",random.randint(90,100))
            # 点击商品库存
        base.send_keys("商品库存","//label[contains(text(),'商品库存：')]/following-sibling::div//input",random.randint(50,60))
            # 点击商品重量
        base.send_keys("点击商品重量","//label[contains(text(),'商品重量：')]/following-sibling::div//input",5)
        # 滚动条
        base.scroll_screen("滚动条")
        # 点击排序
        base.send_keys("点击排序","//label[contains(text(),'排序')]/following-sibling::div//input",random.randint(1,3))
         # 点击下一步
        base.click("点击下一步","//span[contains(text(),'下一步，填写商品促销')]")
        # driver.find_element_by_xpath("//span[contains(text(),'下一步，填写商品促销')]").click()
        time.sleep(1)
        # 填写商品促销 点击预告商品、点击商品上架
        base.send_keys("赠送积分","//label[contains(text(),'赠送积分')]/following-sibling::div/div/input",10)
        base.send_keys("赠送成长值","//label[contains(text(),'赠送成长值')]/following-sibling::div/div/input",5)
        base.send_keys("积分购买限制","//label[contains(text(),'积分购买限制')]/following-sibling::div/div/input",10)
        base.click("预告商品","//label[contains(text(),'预告商品')]/following-sibling::div/div/span")
        base.click("商品上架","//label[contains(text(),'商品上架')]/following-sibling::div/div/span")
        base.click("新品","(//span[contains(text(),'新品')]/following-sibling::div/span)[1]")
        base.click("新品","(//span[contains(text(),'新品')]/following-sibling::div/span)[2]")
        # 服务保证
        base.click("服务保证",'(//label[contains(text(),"服务保证")]/following-sibling::div//span[@class="el-checkbox__inner"])[1]')
        base.click("服务保证",'(//label[contains(text(),"服务保证")]/following-sibling::div//span[@class="el-checkbox__inner"])[2]')
        base.click("服务保证",'(//label[contains(text(),"服务保证")]/following-sibling::div//span[@class="el-checkbox__inner"])[3]')
        # 选择优惠方式
        base.click("特惠促销","//span[contains(text(),'特惠促销')]")
        # 输入时间区间
        base.send_keys("开始时间","//div[contains(text(),'开始时间')]/child::div/input",'2019-04-02')
        base.send_keys("结束时间","//div[contains(text(),'结束时间')]/child::div/input",'2019-05-02')
        # 输入促销价格
        base.send_keys("促销价格","//div[contains(text(),'促销价格')]/child::div/input",50)
        # 点击下一步
        base.click("提交","//span[contains(text(),'下一步，填写商品属性')]")
            # 点击商品属性
        base.click("商品属性","//label[contains(text(),'属性类型：')]/following-sibling::div//input")
        base.click("商品属性","//span[contains(text(),'服装-T恤')]")
        # 填写颜色
        base.send_keys("填写颜色","//span[text()='增加']/parent::*/parent::div//input","黑色")
        # 点击增加
        base.click("点击增加","//span[contains(text(),'增加')]")
        # 选择黑色选项
        base.click("选择黑色","//span[contains(text(),'黑色')]")
        # 点击尺寸
        base.click("点击尺寸","//span[contains(text(),'2XL')]")
        # 滚动条
        base.scroll_screen("滚动条")
        # 输入商品编号
        base.send_keys("输入商品编号","//div[contains(text(),'商品编号')]/following-sibling::div/input",random.randint(2220000,2230000))
        # 点击适用季节
        base.click("适用季节","//div[contains(text(),'适用季节')]/following-sibling::div//input")
        base.click("点击春季","//span[text()='春季']")
        # 点击适用人群
        base.click("适用人群","//div[contains(text(),'适用人群')]/following-sibling::div//input")
        base.click("点击青年","//span[text()='青年']")
        # 点击上市时间
        base.click("上市时间","//div[contains(text(),'上市时间')]/following-sibling::div//input")
        base.click("点击青年", "//span[text()='2018年春']")
        # 点击袖长
        base.click("袖长","//div[contains(text(),'袖长')]/following-sibling::div//input")
        base.click("选择短袖", "//span[text()='短袖']")
        # 上传照片
        # 填写规格参数
        iframe = driver.find_element_by_xpath("(//iframe)[1]")
        driver.switch_to.frame(iframe)
        base.click("点击body","//body[@id='tinymce']")
        base.send_keys("填写规格参数","//body[@id='tinymce']","测试输入")
        driver.switch_to.default_content()
            # 点击下一步
        base.click("提交","//span[contains(text(),'下一步，选择商品关联')]")
            # 点击关联专题
        base.click("关联专题","//span[contains(text(),'轮廓分明')]")
        # base.click("关联专题","//*[@id='app']/div/div[2]/section/div/div/div[5]/form/div[1]/div/div/div[2]/button[2]")
        base.click("关联专题","//label[contains(text(),'关联专题')]/parent::div//button[2]")
            # 点击关联优选
        base.click("关联优选","//label[contains(text(),'关联优选')]/parent::div//span[contains(text(),'待选择')]")
        base.click("导入已选择","//label[contains(text(),'关联优选')]/parent::div//button[2]")
            # 点击完成提交商品
        base.click("提交商品","//span[contains(text(),'完成，提交商品')]")
            # 确认提交
        # driver.switch_to.alert.submit()
        base.click("确定提交","//span[contains(text(),'提示')]/following::div//span[contains(text(),'确定')]")
        time.sleep(3)
        # base.click("确定提交", "/html/body/div[7]/div/div[3]/button[2]/span")
