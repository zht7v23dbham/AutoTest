# -*- coding: utf-8 -*-
import unittest
import time
import os
from Config.running import HTMLTestRunner


test_dir = './'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')



if __name__ == '__main__':

    #定义当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #定义文件路径
    test_dir = os.getcwd()
    # 定义报告输出路径
    htmlPath = test_dir + u'\TestReport\TestReport' + now + u'.html'

    fp = file(htmlPath, "wb")
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"测试用例结果")

    runner.run(discover)  #运行测试用例

    fp.close()  #关闭测试报告
