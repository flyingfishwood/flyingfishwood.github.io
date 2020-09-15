import unittest
import requests
import json

import sys

sys.path.append("../..")
from src.config.config import *
from src.common.readExcel import *
from src.common.case_log import log_case_info
from src.common.con_login import common_header_client, common_header_web


class test_wordpractice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_data.xlsx"), "TestUserLogin")

    def test_getwordpracticelist(self):
        case_data = get_test_data(self.data_list, 'test_getwordpracticelist')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        header = common_header_web()

        res = requests.post(url=url, headers=header, data=data)
        msg = res.json()['msg']

        len1 = len(res.json()['data'])

        if len1 == 0:
            len1 = None

        log_case_info('test_getwordpracticelist', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')
        self.assertIsNotNone(len1, 'fales')


if __name__ == '__main__':
    unittest.main(verbosity=2)
