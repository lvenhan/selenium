# -*- coding:utf-8 -*-
import json
import os
import sys
import time

from selenium.common.exceptions import WebDriverException,NoSuchElementException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Public import LogManager
from page import HomePage

reload(sys)
sys.setdefaultencoding('utf-8')
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
files = os.path.dirname(os.getcwd())
log=LogManager.LogMgr("operation")
class Common():
    u'''
    等待时间
    num: 等待多少秒
    '''
    def sleep(self,num):
        time.sleep(num)

    #浏览器后退操作
    def window_back(self):
        self.driver.back()

    #浏览器前进操作
    def window_forward(self):
        self.driver.forward()

    #页面刷新
    def refresh(self):
        self.driver.refresh()

    # 读取文件路径
    def read_file(self,path,filename):
        filepath=os.path.join(sys.path[1], path, filename)
        if os.path.exists(filepath)==False:
            raise Exception(u"文件不存在")
            self.screenshot("read_file")
        else:
            return filepath
    """
    获取元素
    """
    def getelement(self,type,str):
        self.driver=HomePage.getDriver()
        try:
            if type=="id":
                element=WebDriverWait(self.driver, 20,0.5).until(lambda driver:self.driver.find_element_by_id(str))
            elif type=="name":
                element=WebDriverWait(self.driver, 20 ,0.5).until(lambda driver:self.driver.find_element_by_name(str))
            elif type=="calssname":
                element=WebDriverWait(self.driver,20 ,0.5).until(lambda driver:self.driver.find_element_by_class_name(str))
            elif type=='linktext':
                element=WebDriverWait(self.driver,20 ,0.5).until(lambda driver:self.driver.find_element_by_link_text(str))
            elif type=='xpath':
                element=WebDriverWait(self.driver,20 ,0.5).until(lambda driver:self.driver.find_element_by_xpath(str))
            elif type=='tagname':
                element=WebDriverWait(self.driver,20, 0.5).until(lambda driver:self.driver.find_element_by_tag_name(str))
            return element
        except WebDriverException as e:
            self.screenshot("WebDriverError")
            log.debug(u"WebDriver，error",e)
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")

    """
    根据元素的属性确定点击
    """
    def element_click(self,type, str):
        try:
            element=self.getelement(type,str)
            element.click()
        except:
            log.debug(u"获取element失败")

    #根据元素的属性填写数据
    def element_input(self,type,str,input):
        try:
            element=self.getelement(type,str)
            element.send_keys(input)
        except:
            log.debug(u"输入有误")

    # 根据元素属性选择下拉框数据
    def element_selected(self,type,str,input):
        self.driver=HomePage.getDriver()
        try:
            if type=='index':
                element=WebDriverWait(self.driver,20,0.5).until(lambda driver: driver.find_element_by_xpath(str))
                Select(element).select_by_index(input)
            elif type=='value':
                element=WebDriverWait(self.driver,20,0.5).until(lambda driver:driver.find_element_by_xpath(str))
                Select(element).select_by_value(input)
            elif type=='visibletext':
                element=WebDriverWait(self.driver,20,0.5).until(lambda driver:driver.find_element_by_xpath(str))
                Select(element).select_by_visible_text(input)
        except WebDriverException as e:
            log.debug(u"WebDriver，error",e)
            self.screenshot("WebDriverError")
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")


    #鼠标移动到元素的位置上并点击
    def move_to_element(self,str1,str2):
        self.driver=HomePage.getDriver()
        try:
            #定位到鼠标移动到上面的元素
            element1=WebDriverWait(self.driver,10).until(lambda driver:driver.find_element_by_xpath(str1))
            element2=WebDriverWait(self.driver,10).until(lambda driver:driver.find_element_by_xpath(str2))
            #鼠标悬停在该元素
            ActionChains(self.driver).move_to_element(element1).perform()
            time.sleep(2)
            ActionChains(self.driver).move_to_element(element2).perform()
            element2.click()
        except WebDriverException as e:
            log.debug(u"WebDriver，error",e)
            self.screenshot("WebDriverError")
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")

    #鼠标下拉
    def mouse_pull(self):
        self.driver=HomePage.getDriver()
        try:
            js="var q=document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)
        except:
            raise u"鼠标下滑失败"

    # 截图并保存
    def screenshot(self, filename):
        self.driver= HomePage.getDriver()
        print(files)
        self.driver.get_screenshot_as_file(os.path.join(files,'screenshot',filename+now+'.png'))

    #鼠标移动到元素上并点击
    def move_click(self,type,str):
        self.driver = HomePage.getDriver()
        try:
           ele1=self.getelement(type,str)
           ActionChains(self.driver).move_to_element(ele1).perform()
        except WebDriverException as e:
            log.debug(u"WebDriver，error",e)
            self.screenshot("WebDriverError")
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")

    # 根据find_elements获取集合
    def elements_list(self,type,str):
        self.driver= HomePage.getDriver()
        try:
            if type=="id":
                ele_sum=WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_elements_by_id(str))
            elif type=="classname":
                ele_sum=WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_elements_by_class_name(str))
            else:
                ele_sum=WebDriverWait(self.driver,20 ,0.5).until(lambda driver:driver.find_elements_by_xpath(str))
            return ele_sum
        except WebDriverException as e:
            log.debug(u"WebDriver，error",e)
            self.screenshot("WebDriverError")
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")

    #使用json返回dict/list中文
    def dict_str(self,content):
        return json.dumps(content,encoding="utf-8",ensure_ascii=False,indent=4)

    #输入框根据dict进行传值
    def dict_input(self,type,dict):
        try:
            for k,v in dict.items():
                    self.element_input(type,k,v)
                    self.sleep(0.5)
        except:
            log.debug(u"没有找到对应的元素")
            self.screenshot("input")

    #下拉框通过ID根据dict传值
    def dict_select(self,dict):
        self.driver= HomePage.getDriver()
        try:
            for k,v in dict.items():
                element=WebDriverWait(self.driver,20,0.5).until(lambda driver: driver.find_element_by_id(k))
                Select(element).select_by_index(v)
                time.sleep(1.5)
        except WebDriverException as e:
            log.debug(u"WebDriver，error",e)
            self.screenshot("WebDriverError")
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")

    #清除输入框默认数据
    def clear_input(self,str):
        self.driver= HomePage.getDriver()
        try:
            element=WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element_by_id(str))
            element.clear()
        except WebDriverException as e:
            log.debug(u"WebDriver，error",e)
            self.screenshot("WebDriverError")
        except TimeoutException as e:
            log.error(u"超时",e)
            self.screenshot("TimeException")
        except NoSuchElementException as e:
            log.debug(u"元素异常",e)
            self.screenshot("NoSuchElementException")

    #判断元素是否默认被选中
    def is_Selected(self,type,str):
        try:
            element=self.getelement(type,str)
            if element.is_selected()==False:
                element.click()
            else:
                log.debug(u"元素默认被选中")
        except:
            log.debug(u"元素未被找到")


    #判断元素是否加载显示
    def is_element_visible(self,str):
        try:
            element=self.getelement(type,str)
            if element==False:
                self.sleep(2)
                self.refresh()
            else:
                pass
        except:
            log.debug(u"元素未加载出来")

    #根据输入的顺序输入值（input）
    def orderedDict_input(self,type,dict):
        try:
            for k,v in dict.items():
                self.element_input(type,k,v)
                self.sleep(0.5)
        except:
            log.debug(u"OrderedDict-input")

    #根据输入的顺序点击(click)
    def tuple_click(self,type,tuple):
        try:
            for param in tuple:
                self.element_click(type,param)
                self.sleep(2)
        except:
            log.debug("orderedDict_click")

