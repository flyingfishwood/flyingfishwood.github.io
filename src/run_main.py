'''
Created on 2019年8月5日

@author: SNQU
'''
import unittest
from common.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from common.send_email import send_email
logging.info("=============测试开始============")
suite = unittest.defaultTestLoader.discover(test_path)
with open(report_file,'wb') as f:
    HTMLTestRunner(stream=f,title="Api Test",description="测试描述" ,tester="001").run(suite)
send_email(report_file,receiver)
logging.info("================测试结束============")
   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()