import requests
import json
from src.common.mysql_db import query_db, ucenter_query_db


def login_common():
    parm = {'client_id': 'qiaokao',
            'client_secret': 'VmGM0XOmSbQ452Ajsj23CBgjwS6eKPIZ',
            'grant_type': 'password',
            'password': 'E10ADC3949BA59ABBE56E057F20F883E',
            'scope': 'com.zhl.qk.aphone',
            'username': 15882481462}
    parm2 = json.dumps(parm)
    url = "http://111.204.225.50:8113/d225-8080/zhloauth2-api-project/oauth/token"
    header = {'Accept': 'application/json',
              'Accept-Encoding': 'gzip',
              'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; COL-AL10 Build/HUAWEICOL-AL10)',
              'Content-Type': 'application/json'

              }
    r = requests.post(url, headers=header, data=parm2)

    token = r.json()['data']['access_token']
    return token


def get_token():
    data = ucenter_query_db(
        "SELECT * from oauth_access_token WHERE username=15882481462 ORDER BY create_time DESC LIMIT 1;")

    token = data[0][1]
    is_abandon = 0
    if is_abandon == data[0][9]:

        return token
    elif is_abandon != data[0][9]:
        login_common()
        data = ucenter_query_db(
            "SELECT * from oauth_access_token WHERE username=15882481462 ORDER BY create_time DESC LIMIT 1;")
        token = data[0][1]
        return token
    else:
        raise IndexError
        print('登录出错')


def common_header_client():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android; OS/Android9; '
                      'Terminal/1; zh_CN_#Hans; deviceType/COL-AL10;'
                      ' DeviceId/D42F58BC9409AFC59558C8EFBBAB88B1;'
                      ' Build/HUAWEICOL-AL10; Scope/com.zhl.qk.aphone; '
                      'VersionCode/3061;)',
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip',
        'Authorization': get_token(),
        'Content-Type': 'application/json'
    }
    return headers


def common_header_web():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android; OS/Android9; '
                      'Terminal/1; zh_CN_#Hans; deviceType/COL-AL10;'
                      ' DeviceId/D42F58BC9409AFC59558C8EFBBAB88B1;'
                      ' Build/HUAWEICOL-AL10; Scope/com.zhl.qk.aphone.web; '
                      'VersionCode/3061;)',
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip',
        'Authorization': get_token(),
        'Content-Type': 'application/json;charset=UTF-8'
    }
    return headers


def common_header():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android; OS/Android9; '
                      'Terminal/1; zh_CN_#Hans; deviceType/COL-AL10;'
                      ' DeviceId/D42F58BC9409AFC59558C8EFBBAB88B1;'
                      ' Build/HUAWEICOL-AL10; Scope/com.zhl.qk.aphone; '
                      'VersionCode/3061;)',
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip',

        'Content-Type': 'application/json'
    }
    return headers


def get_code():
    for phone in range(15882481463, 15882481470):

        url = "http://111.204.225.50:8113/d225-8099/zhl-english/api/message/security/applyregist"
        url2 = "http://111.204.225.50:8113/d225-8099/zhl-english/api/message/security/checkmsgcode"
        parms = {"subject_id": 1,
             "op_path": "message.security.applyregist",
             "device_id": "D42F58BC9409AFC59558C8EFBBAB88B1",
             "zhlVaSec": "6677af2cad441a7393b434397cf7d9f3",
             "phone": phone,
             "type": 15, "business_id": 100001,
             "validate": "03def053d17772a2b39a61b148854636"}

        # info = {'phone2': str(phone)}
        requests.post(url, data=json.dumps(parms), headers=common_header())
        sql = "select * from zhl_phone_code where phone=%s; " % (str(phone))
        print(sql)
        # sql2 = sql.format(info)
        # sql2 = (sql, str(phone))
        result = query_db(sql)
        # code = result[0][2]
        print(result)

    #     parms2 = {
    #     "subject_id": 1,
    #     "op_path": "message.security.checkmsgcode",
    #     "code": code,
    #     "zhlVaSec": "38b99e4c873837d5f7dd74c1afd17ca8",
    #     "phone": "15882481462",
    #     "old_phone": 'null', "type": 15,
    #     "business_id": 100001, "validate": "61a2b8a61ec3a2b42d51b45f09997233"
    #
    # }
    #     r = requests.post(url2, data=json.dumps(parms2), headers=common_header())
    #
    #     # code2 = r.json()['data']['code']
    #     # uid = r.json()['data']['uid']
    #     # list2 = [code2, uid]
    #     print(r.json())

    # return list2


def creat_user():
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
    url = "http://111.204.225.50:8113/d225-8099/zhl-english/api/information/userinfo/getusertokenbysmscode"
    res = requests.post(url=url, data=data, header=common_header_client())
    print(res.json())
# creat_user()

get_code()
# def return_token():
#     parm = {'client_id': 'qiaokao',
#             'client_secret': 'VmGM0XOmSbQ452Ajsj23CBgjwS6eKPIZ',
#             'grant_type': 'password',
#             'password': 'E10ADC3949BA59ABBE56E057F20F883E',
#             'scope': 'com.zhl.qk.aphone',
#             'username': 15882481462}
#     parm2 = json.dumps(parm)
#     url = "http://111.204.225.50:8113/d225-8080/zhloauth2-api-project/oauth/token"
#     header = {'Accept': 'application/json',
#               'Accept-Encoding': 'gzip',
#               'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; COL-AL10 Build/HUAWEICOL-AL10)',
#               'Content-Type': 'application/json'
#
#               }
#     r = requests.post(url, headers=header, data=parm2)
#     token = r.json()['data']['access_token']
#     return token
