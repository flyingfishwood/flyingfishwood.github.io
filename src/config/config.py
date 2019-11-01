'''
Created on 2019年8月5日

@author: SNQU

'''
import logging
import os
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(prj_path,'data') #数据目录
test_path = os.path.join(prj_path,'TestCase') #用例目录
log_file = os.path.join(prj_path,'log','log.txt')
report_file = os.path.join(prj_path,'report','report.html')
logging.basicConfig(level=logging.DEBUG,
                                   format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                                   
                                   datefmt='%Y-%m-%d %H:%M:%S',
                                   filename=log_file,
                                   filemode='a' )
# 数据库配置
db_host='119.27.167.20'
db_port=5432
db_user='postgres'
db_passwd = 'postgres'
db = 'qaq_new'

#邮件配置
smtp_server = 'smtp.exmail.qq.com'
smtp_user = 'xiezongliang@snqu.com'
smtp_password = 'DUST0208l'

sender =smtp_user
receiver = '756450141@qq.com'
# receiver = '756450141@qq.com,zhangmi0428@foxmail.com'
subject = '接口测试报告'

