# -*- coding: utf-8 -*-
import unittest
import os
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):

   # def setUp(self):

        #ffdriver = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

        #os.environ["webdriver.firefox.driver"] = ffdriver

        #self.driver = webdriver.Firefox(ffdriver)

    def test(self):
        # firefox 实际安装路径
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("Selenium2")
        self.driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()