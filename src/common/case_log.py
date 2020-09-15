import json
import sys

sys.path.append('..')
from src.config.config import *


def log_case_info(case_name, url, data, expect_res, res):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)
        print(type(data))

    if type(data) == bytes:
        logging.info("测试用例：{}".format(case_name))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format((str(data, 'utf-8'))))
        logging.info("期望结果：{}".format(expect_res))
        logging.info("实际结果：{}".format(res))
    else:
        logging.info("测试用例：{}".format(case_name))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format(data).encode('utf-8').decode('utf-8'))
        logging.info("期望结果：{}".format(expect_res))
        logging.info("实际结果：{}".format(res))
