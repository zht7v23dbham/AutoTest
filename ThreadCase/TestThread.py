#-*- coding: UTF-8 -*-
__author__ = 'zuohaitao'


from threading import Thread

from selenium import webdriver

from time import ctime,sleep

from Drivers import Pysd


def test_baidu(browser,search):
        print('start:%s' % ctime())

        print('browser:%s ,' % browser)


        if browser == "ie":
           driver = webdriver.Ie()
        elif browser == "chrome":
           driver = webdriver.Chrome()
        elif browser == "ff":
           driver = webdriver.Firefox()
        else:
            print("browser参数有误，  只能为 ie 、ff 、chrome")



        Pysd.Pysd.get(browser,"https://www.baidu.com")
        Pysd.Pysd.getElement("kw").send_keys(search)
        Pysd.Pysd.getElement("su").click()
        sleep(2)
        Pysd.Pysd.quit()



if __name__ == "__main__":

    #启动参数 （指定浏览器与百度搜索内容）

    lists = {'chrome': 'seleium', 'ie': 'selenium2', 'ff': 'python'}

    threads = []

    file = range(len(lists))

    #创建线程

    for browser, search in lists.items():
        t = Thread(target=test_baidu, args=(browser, search))
        threads.append(t)
    #启动线程

    for t in file:
        threads[t].start()
    for t in file:
        threads[t].join()

    print('end:%s' % ctime())



