# -*- coding:utf-8 -*-
from selenium import webdriver
import os,sys

def DriverFirefox():
    driver=webdriver.Firefox()
    driver.maximize_window()
    return driver

def Chorme():
    Chorme_file=os.path.join(sys.path[1],'resource', 'chromedriver.exe')
    driver=webdriver.Chrome(Chorme_file)
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def IE():
    Chorme_file=os.path.join(sys.path[1],'resource', 'IEDriverServer.exe')
    driver=webdriver.Chrome(Chorme_file)
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver


