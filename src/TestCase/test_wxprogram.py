
import unittest
import requests
import json
import sys
sys.path.append("../..")
from config.config import *


from common.readExcel import *
from common.case_log import log_case_info
from common.con_login import common_header_02







class test_common_v2_api(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "Testprogram")

    def test_post_newuserdetail(self):
        case_data = get_test_data(self.data_list, 'test_post_newuserdetail')  # 查找用例数据
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, headers=common_header_02(self), data=json.loads(data))
        code = res.json()['code']
        print(res.json())
        log_case_info('test_get_teamurl', url, data, expect_res, code)
        self.assertEqual(code, expect_res, 'false')


if __name__ == '__main__':
    unittest.main(verbosity=2)
