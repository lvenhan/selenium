# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Public import LogManager
from Public import operation

operate=operation.Common()
log=LogManager.LogMgr('close')
class PageCom():

    #用于登陆
    def Publiclogin(self,dict,login):
        #输入用户名密码
        operate.orderedDict_input("id",dict)
        operate.element_click("id",login)
        operate.sleep(2)

    #选择云保类型
    def select_type(self,xpathlink):
        #睡眠2秒，查看数据
        operate.sleep(2)
        #获取场景,根据不同的类别进入到不同的页面
        try:
        #鼠标滑动
            operate.move_click("linktext",u"场景合作")
            operate.element_click("xpath",xpathlink)
        except Exception as e:
            print(e)


