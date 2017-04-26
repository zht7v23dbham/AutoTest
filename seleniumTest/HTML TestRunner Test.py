# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from Config.running import HTMLTestRunner
import sys
import os
import time
from time import sleep

reload(sys)
sys.setdefaultencoding("utf-8")

class BaiduTest(unittest.TestCase):
    """百度首页搜索测试用例"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = u"https://www.baidu.com"
        
    def test_baidu_search(self):
        driver = self.driver
       # print u"开始[case_0001]自动化测试"
        
        driver.get(self.base_url)
        sleep(3)
        # 验证标题
        self.assertEqual(driver.title, u"百度一下，你就知道")
        
        driver.find_element_by_id("kw").clear()
        
        driver.find_element_by_id("kw").send_keys(u"selenium")
        
        driver.find_element_by_id("su").click()
        
        sleep(3)        
        # 验证搜索结果标题
       # self.assertEqual(driver.title, u"selenium_百度搜索")
   
    def tearDown(self):
        self.driver.quit()    
   
        
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduTest('test_baidu_search'))
    #定义当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #定义文件路径
    test_dir = os.getcwd()
    # 定义报告输出路径
    htmlPath = test_dir + u'\TestReport\TestReport' + now + u'.html'

    fp = file(htmlPath, "wb")
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"测试用例结果")
    
    runner.run(testunit)  #运行测试用例
    
    fp.close()  #关闭测试报告
