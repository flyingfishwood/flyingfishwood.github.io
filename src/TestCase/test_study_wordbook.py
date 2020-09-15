import unittest
import requests
import json
import sys

sys.path.append("../..")
from src.config.config import *
from src.common.readExcel import *
from src.common.case_log import log_case_info
from src.common.con_login import common_header_web, common_header_client
from src.common.common_id import get_record_id


class test_study_books(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_data.xlsx"), "TestUserLogin")

    def test_get_math_detail(self):
        case_data = get_test_data(self.data_list, 'test_get_math_detail')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.dumps(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=json.loads(data))
        msg = res.json()['msg']
        log_case_info('test_get_math_detail', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_add_notebook(self):
        case_data = get_test_data(self.data_list, 'test_add_notebook')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.dumps(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=json.loads(data))
        msg = res.json()['msg']
        log_case_info('test_add_notebook', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_delete_noteword(self):
        case_data = get_test_data(self.data_list, 'test_delete_noteword')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = eval(case_data.get('data'))
        # print(type(data))
        # print(type(get_record_id()))
        data2 = {**data, **get_record_id()}
        # print(data2)
        expect_res = case_data.get('expect_res')
        header = common_header_web()
        res = requests.post(url=url, headers=header, data=json.dumps(data2))

        msg = res.json()['msg']
        log_case_info('test_delete_noteword', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')


if __name__ == '__main__':
    unittest.main(verbosity=2)
