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

class test_user_dynamic(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path,"test_user_data.xlsx"), "TestUserLogin")
    def test_a_post_dynamic(self):
        case_data = get_test_data(self.data_list,'test_a_post_dynamic' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        
        res = requests.post(url=url,headers=common_header(self),data=json.loads(data))
        code=res.json()['code']
#         print(res)
        log_case_info('test_a_post_dynamic', url, data, expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def test_b_delete_quanquan(self):
#         i=1
#         for i in range(1,300):    
        case_data = get_test_data(self.data_list,'test_b_delete_quanquan' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        dy_id= common_id.get_user_dynamic_f_id(self)
        print(dy_id)
        expect_res = case_data.get('expect_res')
        datas={'id':dy_id}
        res = requests.post(url=url,headers=common_header(self),data=datas)
        code=res.json()['code']
        print(res.json())
        log_case_info('test_b_delete_quanquan', url, dy_id, expect_res, code)
        self.assertEqual(code, expect_res,'false')
#         i =i+1
          
    def test_get_dynamiclist(self):
        case_data = get_test_data(self.data_list,'test_get_dynamiclist' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        dy_id= common_id.get_user_dynamic_f_id(self)
        print(dy_id)
        expect_res = case_data.get('expect_res')
        datas=case_data.get('data')
        res = requests.post(url=url,headers=common_header(self),data=datas)
        code=res.json()['code']
        print(res.json())
        log_case_info('test_get_dynamiclist', url, dy_id, expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def test_post_dynamic_createtopic(self):
        case_data = get_test_data(self.data_list,'test_post_dynamic_createtopic' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        dy_id= common_id.get_user_dynamic_f_id(self)
         
        expect_res = case_data.get('expect_res')
        datas=case_data.get('data')
        res = requests.post(url=url,headers=common_header(self),data=json.loads(datas))
        code=res.json()['code']
        print(res.json())
        log_case_info('test_post_dynamic_createtopic', url, res,expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def test_get_focus_dynamiclist(self):
        case_data = get_test_data(self.data_list,'test_get_focus_dynamiclist' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        dy_id= common_id.get_user_dynamic_f_id(self)
         
        expect_res = case_data.get('expect_res')
        datas=case_data.get('data')
        res = requests.get(url=url,headers=common_header(self),data=json.loads(datas))
        code=res.json()['code']
        print(res.json())
        log_case_info('test_get_focus_dynamiclist', url, res,expect_res, code)
        self.assertEqual(code, expect_res,'false')
    def test_get_dynamic_detail(self):
        case_data = get_test_data(self.data_list,'test_get_dynamic_detail' )#查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        dy_id= common_id.get_dynamic_list_f_id(self)
         
        expect_res = case_data.get('expect_res')
        datas={'id':dy_id}
        res = requests.get(url=url,headers=common_header(self),params=datas)
        code=res.json()['code']
        print(res.json())
        log_case_info('test_get_dynamic_detail', url, res,expect_res, code)
        self.assertEqual(code, expect_res,'false')                   
                                                
if __name__=='__main__':
    
    unittest.main(verbosity=2)            
                  
            
        


    


