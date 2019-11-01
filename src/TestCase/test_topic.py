'''
Created on 2019年8月12日

@author: SNQU
'''
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
from common.con_login import common_header
from common import common_id

class test_topic(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path,"test_user_data.xlsx"), "TestUserLogin")
    def test_get_topic_list(self):
        case_data = get_test_data(self.data_list,'test_get_topic_list' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
       
        res = requests.get(url=url,headers=common_header(self),data=json.loads(data))
        code=res.json()['code']
#         print(res.json())
        log_case_info('test_get_topic_list', url, data, expect_res, code)
        self.assertEqual(code, expect_res,'false')
     
    def test_get_topic_detail(self):
        case_data = get_test_data(self.data_list,'test_get_topic_detail' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
       
        res = requests.get(url=url,headers=common_header(self),params=json.loads(data))
        code=res.json()['code']
#         print(res.json())
        log_case_info('test_get_topic_detail', url, data, expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def test_get_official_topictags(self):
        case_data = get_test_data(self.data_list,'test_get_official_topictags' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
       
        res = requests.get(url=url,headers=common_header(self),params=json.loads(data))
        code=res.json()['code']
#         print(res.json())
        log_case_info('test_get_official_topictags', url, data, expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def test_listsbytopic(self):
        case_data = get_test_data(self.data_list,'test_listsbytopic' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
       
        res = requests.get(url=url,headers=common_header(self),params=json.loads(data))
        code=res.json()['code']
#         print(res.json())
        log_case_info('test_listsbytopic', url, data, expect_res, code)
        self.assertEqual(code, expect_res,'false')    
if __name__=='__main__':
    unittest.main(verbosity=2)            
                  
            
        


    



