# -*- coding:utf-8 -*-
import unittest
from collections import OrderedDict

from Public import LogManager
from Public import operation
from page import comMethod, HomePage, accountManage

operate=operation.Common()
pagecom=comMethod.PageCom()
log=LogManager.LogMgr('meixing')
accm=accountManage.accountM()
class MeiXing(unittest.TestCase):
    u"""美行"""
    def test_Login(self):
        u"""登陆"""
        #打开浏览器，并登陆
        HomePage.HomePage(self)
        #登陆渠道
        operate.element_click("xpath","//div[@class='right nav-box clearfix']/a[@data-toggle='modal']")
        operate.sleep(2)
        self.name='mxtest'
        self.password='123456'
        login_input=OrderedDict([('tel2',self.name),
            ('password2','123456')])
        pagecom.Publiclogin(login_input,"channel-login-btn")
        operate.sleep(2)
        #判断是否登陆是否获取到用户名
        try:
            get_user=operate.getelement("id","span-userName")
            self.assertEqual(self.name,get_user.text,u"登陆失败")
        except:
            log.debug(u"登陆失败")
            operate.screenshot("meixing-login")

    #创建账号
    def test_Addaccount(self):
        #进入账号管理页面
        operate.element_click("xpath",".//*[@id='sidebar']/ul/li[@data-href='user.html']")
        #读csv，批量添加账号添加账号
        accm.addAccount()
        #判断是否添加成功
        name_all=operate.elements_list("xpath",".//*[@id='dynamic-table']/tbody/tr")
        print(name_all.text)

    #创建保单
    def test_Policycreate(self):
        u"""创建保单"""
        #进入创建保单
        create=".//*[@id='sidebar']/ul/li[@data-href='order.html']"
        operate.element_click("xpath",create)
        operate.sleep(2)
        operate.refresh()
        #产品类别和保险公司默认：出境保险和大地保险
        #选择产品名称,（默认计划一）目的地
        #页面刷新
        dict_select={"form-product":3,"form-package":0, "form-address":2,"form-insure-day":7}
        operate.dict_select(dict_select)
        #输入团号
        operate.element_input("id","form-teamId","ERMED1234")
        #选择生效时间,默认选择下一个月的第一天
        time_tuple=(".//*[@id='form-product-info']//div[@class='col-xs-4 time-group'][1]//span[@class='input-group-addon']",
                    "//th[@class='next']",
                    "//tr[1]/td[@class='day'][1]")
        operate.tuple_click("xpath",time_tuple)
        #查看投保提示和保障详情
        link=('.//*[@id="link-tips"]',
              './/*[@id="yb_ddhly_tips"]//button[@class="close"]',
              './/*[@id="link-detail"]',
              './/*[@id="modal-form-detail"]//button[@class="close" and @type="button"]')
        operate.tuple_click("xpath",link)
        #操作投保人信息
        try:
            #导入投保人信息,获取投保人文件路径
            self.addperson()
            #删除投保人，留一个投保人
            # delect_touple=("select-all","delete-select")
            # operate.element_click("id",delect_touple)
            #确认投保
            operate.sleep(2)
            operate.element_click("id","btn-order")
        except:
            log.debug(u"操作投保人信息错误")
        #判断是否进入确认页面
        try:
            title=operate.getelement("xpath",".//*[@id='profile-user-info']//span[@data-field='count']")
            print(title.text)
            nums=operate.elements_list("xpath",".//*[@id='table-userlist']/tbody/tr")
            print(str(len(nums)))
            self.assertEqual(title.text,str(len(nums)),u"投保页面错误")
        except:
            log.debug(u"确认投保页面错误")
        #等待3秒，查看数据是否完整
        operate.sleep(3)
        operate.element_click("id","form-btn-order")
        #打印投保返回信息
        result=operate.getelement("xpath",".//*[@id='anyi-modal-alert']//div[@class='modal-body']")
        print(result.text)
        operate.sleep(1)
        operate.element_click("xpath",".//*[@id='anyi-modal-alert']//div[@class='modal-footer']/a")

    #添加投保人
    def addperson(self):
        try:
            filepath=operate.read_file("testData","mxtoubao.xlsx")
            operate.element_click("id","btn-import")
            operate.element_input("id","form-field-attach1",filepath)
            #关闭弹层
            operate.element_click("xpath",".//*[@id='modal-form-upload']//div[@class='modal-content']//button[@class='btn btn-sm']")
            operate.sleep(2)
        except:
            log.debug(u"增加被保人错误")


if __name__ == '__main__':
    #创建测试集
    suite=unittest.TestSuite()
    suite.addTest(MeiXing("test_Login"))
    suite.addTest(MeiXing("test_Addaccount"))
    suite.addTest(MeiXing("test_Policycreate"))

    #执行测试集
    runner=unittest.TextTestRunner()
    runner.run(suite)

