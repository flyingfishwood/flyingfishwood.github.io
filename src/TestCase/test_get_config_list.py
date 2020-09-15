import unittest
import requests
import json
import sys

sys.path.append("../..")
from src.config.config import *
from src.common.readExcel import *
from src.common.case_log import log_case_info
from src.common.con_login import common_header_client, common_header_web
import threading


class test_get_config_list(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_data.xlsx"), "TestUserLogin")

    def test_get_video_list(self):
        case_data = get_test_data(self.data_list, 'test_get_video_list')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.dumps(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        header = common_header_web()
        res = requests.post(url=url, headers=header, data=json.loads(data))
        msg = res.json()['msg']
        log_case_info('test_get_video_list', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_ad_config(self):
        case_data = get_test_data(self.data_list, 'test_get_ad_config')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.dumps(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        header = common_header_web()
        res = requests.post(url=url, headers=header, data=json.loads(data))
        msg = res.json()['msg']
        log_case_info('test_get_ad_config', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_student_version_list(self):
        case_data = get_test_data(self.data_list, 'test_get_student_version_list')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.dumps(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        header = common_header_web()
        res = requests.post(url=url, headers=header, data=json.loads(data))
        msg = res.json()['msg']
        log_case_info('test_get_student_version_list', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_student_info(self):
        case_data = get_test_data(self.data_list, 'test_get_student_info')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')

        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=data)

        msg = res.json()['msg']
        log_case_info('test_get_student_info', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_userlearningproductlist(self):
        case_data = get_test_data(self.data_list, 'test_get_userlearningproductlist')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')

        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=data)

        msg = res.json()['msg']
        log_case_info('test_get_userlearningproductlist', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_usermemberinfov2(self):
        case_data = get_test_data(self.data_list, 'test_get_usermemberinfov2')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')

        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=data)

        msg = res.json()['msg']
        log_case_info('test_get_usermemberinfov2', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_getmembercenterhome(self):
        case_data = get_test_data(self.data_list, 'test_getmembercenterhome')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')

        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=data)

        msg = res.json()['msg']
        log_case_info('test_getmembercenterhome', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_allvoicelivelist(self):
        case_data = get_test_data(self.data_list, 'test_get_allvoicelivelist')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')

        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=data)

        msg = res.json()['msg']
        log_case_info('test_get_allvoicelivelist', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_get_rewardresult(self):
        case_data = get_test_data(self.data_list, 'test_get_rewardresult')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')

        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=data)

        msg = res.json()['msg']
        log_case_info('test_get_rewardresult', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')


if __name__ == '__main__':
    unittest.main(verbosity=2)
