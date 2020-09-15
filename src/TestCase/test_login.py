import unittest
import requests
import json
import sys

sys.path.append("../..")
from src.config.config import *
from src.common.readExcel import *
from src.common.case_log import log_case_info
from src.common.con_login import common_header_client, get_code


class test_user_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_data.xlsx"), "TestUserLogin")

    def test_pwd_login(self):
        case_data = get_test_data(self.data_list, 'test_pwd_login')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.dumps(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=json.loads(data))
        msg = res.json()['msg']
        log_case_info('test_pwd_login', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')

    def test_capcth_login(self):
        case_data = get_test_data(self.data_list, 'test_capcth_login')  # 查找用例数据

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = {
            "subject_id": 1,
            "uid": get_code()[1],
            "op_path": "information.userinfo.getusertokenbysmscode",
            "code": get_code()[0],
            "zhlVaSec": "1224377d441ac4218e30494dba29b0e3",
            "business_id": 100001,
            "client_id": "qiaokao",
            "validate": "e451a04e48dfb27ad1329139db74d9cc"

        }
        expect_res = case_data.get('expect_res')
        header = common_header_client()
        res = requests.post(url=url, headers=header, data=json.dumps(data))
        # print(res.json())
        msg = res.json()['msg']
        log_case_info('test_capcth_login', url, data, expect_res, msg)
        self.assertEqual(expect_res, msg, 'false')


if __name__ == '__main__':
    unittest.main(verbosity=2)
