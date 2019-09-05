# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import Driver

def HomePage(self):
    global driver
    #打开浏览器，进入首页
    self.driver=Driver.DriverFirefox()
    driver=self.driver
    driver.get("http://test.spb.riskeys.com")
    time.sleep(1)
    # 判断是否是首页内容
    try:
        self.assertEquals(u"安逸云保-场景化保险专家",driver.title,"title error")
    except AssertionError as e:
        print u"找不到这个标题"

def getDriver():
    return driver

#关闭当前页面
def closePage(self):
    try:
        time.sleep(2)
        self.driver= HomePage.getDriver()
        ActionChains(self.driver).send_keys(Keys.CONTROL,'W').perform()
    except:
        print(u"关闭浏览器失败")

