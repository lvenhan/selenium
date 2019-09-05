# -*- coding:utf-8 -*-
import os,sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://test.spb.riskeys.com")
# from selenium.webdriver.common.keys import Keys
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('W').perform()
# ActionChains(driver).send_keys(Keys.CONTROL,'W').perform()
# driver.find_element_by_xpath("//img[@class='logo']").send_keys(Keys.CONTROL,'W')

ele=driver.find_element_by_link_text("场景合作")
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_xpath("//div[@class='scene-box left']/ul/li[1]/a").click()

# elments=driver.find_elements_by_xpath("//div[@class='scene-box left']/ul/li")
# text=[]
# for menu in elments:
#     pass
#
# from Public import LogManager
#
# log=LogManager.LogMgr("testfail")
# a=1
# if a==2:
#     print("a=1")
# else:
#     log.debug("a!=1")
#     print("a!=1")



# from datetime import datetime
# now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(now+".log")


from collections import OrderedDict

# link=OrderedDict([('id','link-tips'),
#                 ('xpath','.//*[@id="yb_ddhly_tips"]//button[@class="close"]'),
#                 ('id','link-detail'),
#                 ('xpath','.//*[@id="modal-form-detail"]//button[@class="close" and @type="button"]')
#         ])
# link=OrderedDict(
#              [('YANGWANZHA',80),('YANGWANZHA',70),('shanghai',90),('nanjing',60),
#          ('guangzhou',55),('hangzhou',88),('yangzhou',44),('qinghai',99),
#          ('langfang',77),('shijiazhuang',66),('kunming',35),('suzhou',98)
#              ])
# for k,v in link.items():
# 	print k,v

# tuple=('.//*[@id="link-tips"]','.//*[@id="yb_ddhly_tips"]//button[@class="close"]',
#               './/*[@id="link-detail"]','.//*[@id="modal-form-detail"]//button[@class="close" and @type="button"]')
# for i in tuple:
#     print(i)


