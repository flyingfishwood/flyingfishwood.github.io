'''
Created on 2019年8月5日

@author: SNQU
'''
import unittest
import requests
import json
import sys
sys.path.append("../..")
from config.config import *
from common.readExcel import *
from common.case_log import log_case_info
from common.con_login import login_common

class test_user_login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path,"test_user_data.xlsx"), "TestUserLogin")
    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list,'test_user_login_normal' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
        res = requests.post(url=url,headers=header,data=json.loads(data))
        code=res.json()['code']
        log_case_info('test_user_login_normal', url, data, expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def  test_user_login_password_wrong(self):
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
        res = requests.post(url= url,headers=header,data = json.loads(data))
        code=res.json()['code']
#         print(res.json())
        log_case_info('test_user_login_password_wrong',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_third_login_wx(self):
        case_data = get_test_data(self.data_list, 'test_user_third_login_wx')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
        code=res.json()['code']
        log_case_info('test_user_third_login_wx',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_third_login_qq(self):
        case_data = get_test_data(self.data_list, 'test_user_third_login_qq')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
        code=res.json()['code']
#         print(res.json())
        log_case_info('test_user_third_login_qq',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_third_login_wb(self):
        case_data = get_test_data(self.data_list, 'test_user_third_login_wb')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_third_login_wb',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_bphone(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_bphone')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_bphone',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_Retrieve_password(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_Retrieve_password')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_Retrieve_password',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_reg(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_reg')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_reg',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_changephone(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_changephone')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios',
            'token':login_common(self)}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_changephone',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_captchalogin(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_captchalogin')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_captchalogin',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_answer(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_answer')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_answer',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_set_tradepd(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_set_tradepd')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_set_tradepd',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_sms_get_change_tradepd(self):
        case_data = get_test_data(self.data_list, 'test_user_sms_get_change_tradepd')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios'}
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_sms_get_change_tradepd',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')
    def  test_user_membertags(self):
        case_data = get_test_data(self.data_list, 'test_user_membertags')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        token =login_common(self)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'device-type':'ios',
            'token':token
        }
           
        res = requests.post(url= url,headers=header,data = json.loads(data))
#         print(res.json())
        code=res.json()['code']
            
        log_case_info('test_user_membertags',url,data,expect_res,code)
        self.assertEqual(code, expect_res, 'false')                                                
if __name__=='__main__':
    unittest.main(verbosity=2)            
                  
            
        


    


