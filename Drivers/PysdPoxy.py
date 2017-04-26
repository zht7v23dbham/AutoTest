#-*- coding: UTF-8 -*-
__author__ = 'zuohaitao'

from selenium import webdriver
from selenium.webdriver.common.proxy import *



PROXY = "localhost:8088"


desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()

desired_capabilities['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "noProxy":  None,
        "proxyType":    "MANUAL",
        "class":    "org.openqa.selenium.Proxy",
        "autodetect":   False
}


