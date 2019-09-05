# -*- coding:utf-8 -*-
import unittest

from collections import OrderedDict
from Public import LogManager
from Public import operation
from page import comMethod, HomePage

compage=comMethod.PageCom()
operate=operation.Common()
log=LogManager.LogMgr('yunbao-wpb')
class QueryPrice(unittest.TestCase):
    u"""用户投保流程"""
    def testEnquiry(self):
        u"""询价"""
        #打开首页并且登陆账号
        HomePage.HomePage(self)
        operate.sleep(2)
        operate.move_click("linktext",u"场景合作")
        operate.element_click("xpath","//a[@href='/landing/shop.html']")
        self.driver= HomePage.getDriver()
        #立即进入
        operate.element_click("linktext",u"立即进入")
        operate.sleep(2)
        #断言是否进入到首页
        try:
            self.assertEqual("http://test.spb.riskeys.com/shop/index.html",
                             self.driver.current_url,
                             "page is error")
        except :
            log.debug(u"进入首页失败")

        #登陆
        # self.login()
        #进入我要询价
        # 将页面下来，再次询价
        # operate.mouse_pull()
        operate.element_click("id","begin-buy")
        operate.sleep(2)
        #调用ask方法，进行询价
        QueryPrice.ask(self)

    def testScheme(self):
        u"""询价方案"""
        operate.sleep(2)
        #下拉页面到
        operate.mouse_pull()
        dict={'insuranceTime':1,'perNumber':1}
        operate.dict_select(dict)
        #先清楚文本框默认数字，再输入
        operate.clear_input("staffNumber")
        operate.element_input("id","staffNumber",3)
        operate.sleep(2)
        check="//div[@class='form-content container']/div[@class='button-box']/div[@class='notice']/span[1]"
        operate.element_click("xpath",check)
        #立即投保
        operate.element_click("id","buy-btn")
        operate.sleep(1)

    def test_Insure(self):
        u"""开始投保"""
        #默认选择企业
        #输入投保机构，联系人，手机号码
        insure_dict={'shopName':'TaiPingYang','contacts':'testone','insurer-phone':'18207278423'}
        operate.dict_input("id",insure_dict)
        #传入员工名单
        #获取excel路径
        fpath=operate.read_file("testData","mingdan.xlsx")
        operate.element_input("id","form-field-attach",fpath)
        operate.sleep(2)
        #鼠标下滑到最下面
        operate.mouse_pull()
        #选择发票类型
        xpath="//input[@type='radio' and @value='normal']"
        operate.element_click("xpath",xpath)
        dict_receiver={"receiverName":"Hanxiao","receiverTel":"18207278423","receiverPost":"200000"}
        operate.dict_input("id",dict_receiver)
        operate.element_input("id","receiverAddress",u"上海市浦东新区")
        #确认投保
        operate.mouse_pull()
        check_radio="//div[@class='button-box']/div[@class='notice']/span[@class='my-check']"
        operate.element_click("xpath",check_radio)
        operate.element_click("id","buy-btn")
        #确认投保信息，并判断是否是投保页面，是则确认投保，不是则刷新页面
        operate.sleep(2)
        try:
            #判断"投保确认"元素是否存在于页面
            text= HomePage.getDriver().find_element_by_xpath("//div[@class='block-title']")
            if(text.is_displayed()==True):
                if(text.text==u'确认投保'):
                    print(u"成功进入投保确认页面")
                else:
                    operate.refresh()
            else:
                operate.refresh()
        except:
            log.debug(u"页面元素未找到")
        #确认页面之后确认投保
        operate.mouse_pull()
        operate.is_Selected("xpath","//div[@class='button-box']/div[@class='notice']/span[@class='my-check']")
        operate.element_click("id","buy-btn")
        self.login()
        operate.element_click("id","buy-btn")
        operate.sleep(3)


    def test_Pay(self):
        u"""支付"""
        #判断是否是支付页面
        operate.sleep(2)
        self.driver= HomePage.getDriver()
        element=operate.getelement("xpath","//a[@class='logo']")
        try:
            if element.is_displayed()==True: #页面加载出来
                operate.sleep(1)
                operate.element_click("xpath",".//div[@title='模拟网银']")
                #确认网银支付
                operate.element_click("xpath",".//div[@class='action']/a")
                result=operate.getelement("tagname","h3")
                #如果支付失败：则print出原因
                if result.is_displayed()==True:
                    reason=operate.getelement("tagname","p")
                    print(result.text)
                    print(reason.text)
                    operate.screenshot("orderpay")
                    #关不标签页
                    HomePage.closePage()
                else:
                    HomePage.closePage()
            else:
                log.debug(u"进入支付页面失败")
                operate.screenshot("payPage")
                HomePage.closePage()
        except:
            log.warning(u"支付失败")

    #登陆
    def login(self):
        operate.sleep(2)
        login_input=OrderedDict([('account','testone'),
            ('password','123456')])
        compage.Publiclogin(login_input,"user-login")

    def ask(self):
        #判断是否是询价页面
        try:
            self.assertEqual("http://test.spb.riskeys.com/shop/ask.html",
                             self.driver.current_url,
                             "page is error")
        except :
            log.debug(u"进入询价页面失败")
        #使用for循环，依次输入下拉框数据
        markets=operate.elements_list("xpath", ".//*[@id='city']/select")
        for num in range(1,len(markets)+1):
            market_name=".//*[@id='city']/select["+str(num)+"]"
            operate.element_selected("index",market_name,1)
            operate.sleep(1)
        #传入字典输入商铺号以及商铺名称
        dict_v={'shopId':'SPH001','shopName':'TEST_SHOP'}
        operate.dict_input("id",dict_v)
        #输入商铺面积，设备价值，存货价值
        dict_price={'shopSize':2,'shopDeviceValue':3,'shopStockValue':2}
        operate.dict_select(dict_price)
        #输入装修合同
        operate.element_selected("index",".//*[@id='shopDecorationTotal']/select",2)
        #点击为您推荐
        operate.element_click("id","submit-answers")
        operate.sleep(2)


if __name__ == '__main__':
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(QueryPrice("testEnquiry"))
    suite.addTest(QueryPrice("testScheme"))
    suite.addTest(QueryPrice("test_Insure"))

    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)
