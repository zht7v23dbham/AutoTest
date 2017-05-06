# -*- coding: utf-8 -*-
#import unittest
from selenium import webdriver
import os
from time import sleep

if __name__ == '__main__':

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    iedriver=parent_path+"\Drivers\IEDriverServerX64.exe"
    print iedriver

    os.environ["webdriver.ie.driver"] = iedriver #设置环境变量
    print iedriver
    driver = webdriver.Ie(iedriver)
    #os.environ["webdriver.ie.driver"] = iedriver
    # driver = webdriver.Ie(executable_path=iedriver)

    sleep(10)
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("Selenium2")
    driver.find_element_by_id("su").click()
    sleep(10)
    driver.close()
    driver.quit()


