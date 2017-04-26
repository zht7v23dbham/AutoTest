#-*- coding:utf-8 -*-
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command





import os

class Pysd(object):


    def __init__(self, browser='ff'):
         '''
         Run class initialization method, the default is proper
         to drive the Firefox browser. Of course, you can also
         pass parameter for other browser, Chrome browser for the "Chrome",
         the Internet Explorer browser for "internet explorer" or "ie".
         '''
         if browser == "firefox" or browser == "ff":
             driver = webdriver.Firefox()
         elif browser == "chrome":
             driver = webdriver.Chrome()
         elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
         elif browser == "opera":
             driver = webdriver.Opera()
         elif browser == "phantomjs":
             driver = webdriver.PhantomJS()
         elif browser == 'edge':
             driver = webdriver.Edge()
         try:
             self.driver = driver
         except Exception:
             raise NameError("Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)


    def getElement(self, selector):

        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

#定位单个元素封装

    def findId(self,id):

        f = self.driver.find_element_by_id(id)
        return f

    def findName(self,name):
        f = self.find_element_by_name(name)
        return f

    def findClassName(self, name):
        f = self.find_element_by_class_name(name)
        return f

    def findTagName(self, name):
        f = self.find_element_by_tag_name(name)
        return f

    def findLinkText(self, text):
        f = self.find_element_by_link_text(text)
        return f

    def findPLinkText(self, text):
        f = self.find_element_by_partial_link_text(text)
        return f

    def findXpath(self, xpath):
        f = self.find_element_by_xpath(xpath)
        return f

    def findCss(self, css):
        f = self.find_element_by_css_selector(css)
        return f
#定位一组元素封装'''

    def findsId(self, id):
        f = self.find_elements_by_id(id)
        return f

    def findsName(self, name):
        f = self.find_elements_by_name(name)
        return f

    def findsClassName(self, name):
        f = self.find_elements_by_class_name(name)
        return f

    def findsTagName(self, name):
        f = self.find_elements_by_tag_name(name)
        return f

    def findsLinkText(self, text):
        f = self.find_elements_by_link_text(text)
        return f

    def findsPLinkText(self, text):
        f = self.find_elements_by_partial_link_text(text)
        return f

    def findsXpath(self, xpath):
        f = self.find_elements_by_xpath(xpath)
        return f

    def findsCss(self, css):
        f = self.find_elements_by_css_selector(css)
        return f


    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self.getElement(selector)
        el.clear()
        el.send_keys(text)

    def open (self, url):

        self.open(url)


    def get (self, url):

        self.get(url)



    #
    # def find_element_by_id(self,id_):
    #
    #
    #         #ID = "id"
    #         #XPATH = "xpath"
    #         #LINK_TEXT = "link text"
    #         #PARTIAL_LINK_TEXT = "partial link text"
    #         #NAME = "name"
    #         #TAG_NAME = "tag name"
    #         #CLASS_NAME = "class name"
    #         #CSS_SELECTOR = "css selector"
    #
    #     return self.find_element_by_id(by=By.ID,value=id_)


    def maxwindow (self):
        #  最大化 窗口
        self.driver.maximize_window()


    def setwindow (self,wide, high):
        #  设置 窗口
        self.driver.set_window_size(wide, high)

    def F5 (self):
        #  浏览器刷新
        self.driver.refresh()

    def back(self):
        #  浏览器前进  后退

        self.driver.back()

    def forward(self):
        #  浏览器前进
        self.driver.forward()

    def quit(self):
        #
        self.driver.quit()

    def close(self):
        #关闭其中窗口
        self.driver.close()

#鼠标事件

    def double_click(self, double_click):
        #双击鼠标
        ActionChains(driver).double_click(double_click).perform()

    def above (self, above):
        #鼠标 悬停
        ActionChains(driver).move_to_element(above).perform()

    def drag_and_drop(self, source, target):
        #拖放 操作
        ActionChains(driver).drag_and_drop(source, target).perform()

   #    #键盘操作
   # def send_keys(self, keys):
   #
   #              keys = Keys.ALT
   #              keys = Keys.NULL         = '\ue000'
   #          CANCEL       = '\ue001' #  ^break
   #          HELP         = '\ue002'
   #          BACKSPACE    = '\ue003'
   #          BACK_SPACE   = BACKSPACE
   #          TAB          = '\ue004'
   #          CLEAR        = '\ue005'
   #          RETURN       = '\ue006'
   #          ENTER        = '\ue007'
   #          SHIFT        = '\ue008'
   #          LEFT_SHIFT   = SHIFT
   #          CONTROL      = '\ue009'
   #          LEFT_CONTROL = CONTROL
   #          ALT          = '\ue00a'
   #          LEFT_ALT     = ALT
   #          PAUSE        = '\ue00b'
   #          ESCAPE       = '\ue00c'
   #          SPACE        = '\ue00d'
   #          PAGE_UP      = '\ue00e'
   #          PAGE_DOWN    = '\ue00f'
   #          END          = '\ue010'
   #          HOME         = '\ue011'
   #          LEFT         = '\ue012'
   #          ARROW_LEFT   = LEFT
   #          UP           = '\ue013'
   #          ARROW_UP     = UP
   #          RIGHT        = '\ue014'
   #          ARROW_RIGHT  = RIGHT
   #          DOWN         = '\ue015'
   #          ARROW_DOWN   = DOWN
   #          INSERT       = '\ue016'
   #          DELETE       = '\ue017'
   #          SEMICOLON    = '\ue018'
   #          EQUALS       = '\ue019'
   #
   #          NUMPAD0      = '\ue01a' #  number pad keys
   #          NUMPAD1      = '\ue01b'
   #          NUMPAD2      = '\ue01c'
   #          NUMPAD3      = '\ue01d'
   #          NUMPAD4      = '\ue01e'
   #          NUMPAD5      = '\ue01f'
   #          NUMPAD6      = '\ue020'
   #          NUMPAD7      = '\ue021'
   #          NUMPAD8      = '\ue022'
   #          NUMPAD9      = '\ue023'
   #          MULTIPLY     = '\ue024'
   #          ADD          = '\ue025'
   #          SEPARATOR    = '\ue026'
   #          SUBTRACT     = '\ue027'
   #          DECIMAL      = '\ue028'
   #          DIVIDE       = '\ue029'
   #
   #          F1           = '\ue031' #  function  keys
   #          F2           = '\ue032'
   #          F3           = '\ue033'
   #          F4           = '\ue034'
   #          F5           = '\ue035'
   #          F6           = '\ue036'
   #          F7           = '\ue037'
   #          F8           = '\ue038'
   #          F9           = '\ue039'
   #          F10          = '\ue03a'
   #          F11          = '\ue03b'
   #          F12          = '\ue03c'
   #
   #          META         = '\ue03d'
   #          COMMAND      = '\ue03d'
   #
   #
   #
   #           self.send_keys(keys)
   #


#显示等待
    def WebDWait(self, timeout, poll_frequency, ignored_exceptions):

        self.driver.WebDriverWait(self, 5, 0.5)
#隐式等待

    def imwait(self, time):

        self.driver.implicitly_wait(time)

#多窗口切换

    def switch_to(self):

        self.driver.switch_to.window()

#cookie操作

    def getcookie(self):
        #获取 cookie
        self.driver.get_cookie()

    def addcookie(self):
        #添加 cookie
        self.driver.add_cookie()

    def deletecooike(self, cookie):
        #删除指定的
        self.driver.delete_cookie(cookie)

    def deleteallcookie(self):
        #删除删除所有 cookie
        self.driver.delete_all_cookies()
#鼠标移动

    def moveoffset(self):

        ActionChains(self.driver).move_by_offset(2, 0).perform()

#设置超时



    def pagetimeout(self, timewait):
        #设置页面加载超时时间
        self.driver.set_page_load_timeout(self, timewait)


    def scripttimeout(self, timewait):
        #设置脚本执行超时时间
        self.driver.set_script_timeout(self, timewait)



# 操作截图
    def insert_img(self, file_name):
    # 截图
        base_dir = os.path.dirname(os.path.dirname(__file__))

        base_dir = str(base_dir)

        base_dir = base_dir.replace('\\','/')

        base = base_dir.split('/test_case')[0]

        file_path = base + "" + file_name

        self.get_screenshot_as_file(file_path)









if __name__ == '__main__':

    driver = Pysd("chrome")