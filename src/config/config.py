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
db_host = '192.168.101.153'
db_port = 3306
db_user = 'zhl_mcenter'
db_passwd = 'mcenter&2$7'
db = 'zhl_mcenter'
ucenter_db_host = '192.168.101.153'

User_db_name = 'zhl_user'
user_db_passwd='zhluser#9.4'
user_db = 'zhl_ucenter'


#邮件配置
smtp_server = 'smtp.exmail.qq.com' #第三方邮件服务器
smtp_user = 'xiezongliang@zhihuiliu.com' #个人邮箱账号密码
smtp_password = 'DUST0208l'

sender =smtp_user
receiver = '756450141@qq.com'#接收方
# receiver = ''
subject = '接口测试报告'

