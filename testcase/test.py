# coding=utf-8
import unittest
import os
import requests

class testTest(unittest.TestCase):
    def setUp(self):
        #请求头信息
        self.headers = {}
    def test_test_normal0(self):
        url = 'https://api.bs.pre.gomeplus.com/v3/user/loginTokenGenerateForTestAction'
        r = requests.get(url,params={'userId,app': '100036366285'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
    def test_test_normal1(self):
        url = 'https://api.bs.pre.gomeplus.com/v3/user/loginTokenGenerateForTestAction'
        r = requests.get(url,params={'userId,app': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
    def test_test_fault0(self):
        url = 'https://api.bs.pre.gomeplus.com/v3/user/loginTokenGenerateForTestAction'
        r = requests.get(url,params={'userId,app': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
