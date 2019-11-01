'''
Created on 2019年8月7日

@author: SNQU
'''
import requests
from common.con_login import * 
# global  header 
# header=common_header(self)
def get_dynamic_list_f_id(self):
    header=common_header(self)
    url = 'http://119.27.167.20:8083/dynamic/lists.json'
    re = requests.get(url,headers=header)
    dynamic_id = re.json()['data']['data'][0]['_id']
    return dynamic_id
def get_user_dynamic_f_id(self):
    header=common_header(self)
    url = 'http://119.27.167.20:8083/member/dynamiclists.json'
    re = requests.get(url, headers = header)
    user_dynamic_id = re.json()['data']['data'][0]['_id']
    return user_dynamic_id
def get_user_demand_id(self):
    header=common_header(self)
    url = 'http://119.27.167.20:8083/demand/otherList.json'
    re = requests.get(url, headers = header)
    user_demand_id = re.json()['data']['data'][0]['_id']
    return user_demand_id

    
    