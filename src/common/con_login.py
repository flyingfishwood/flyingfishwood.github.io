
import requests

def login_common(self):
    parm={'telephone':'15882481462','captcha':'123456'}
    url ="http://119.27.167.20:8083/member/login.json"
    r = requests.post(url,data=parm)
    token=r.json()['data']['token']
       
    return token
def common_header(self):
     
         
         
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':login_common(self),
            'device-version':'2.5.1',
            'device-type':'ios'
        }
    return headers
