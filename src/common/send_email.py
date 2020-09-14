'''
Created on 2019年8月5日

@author: SNQU
'''
import smtplib
from email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
sys.path.append('..')
from src.config.config import *
def send_email(report_file,to_addr_in):
    to_addr = to_addr_in
    to_addrs = to_addr.split(',')##解析邮件地址
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))
    msg['From'] = 'xiezongliang@zhihuiliu.com'
#     msg['To'] = 'zhangmi0428@foxmail.com'
#     msg['To'] = '756450141@qq.com'
#     msg['To'] = '1641401365@qq.com'
    msg['To'] = ",".join(to_addrs)
    msg['Subject'] = Header(subject,'utf-8')
    attl = MIMEText(open(report_file,'rb').read(),'base64','uft-8')
    attl["Content-Type"] = 'application/octet-stream'
    attl["Content-Disposition"] = 'attachment;filename="{}"'.format(report_file)
    msg.attach(attl)
    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_password)
        smtp.sendmail(sender,to_addrs,msg.as_string())
        logging.info("邮件发送完成")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
#
# send_email(report_file,receiver)