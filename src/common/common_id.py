'''
Created on 2019年8月7日

@author: SNQU
'''
from src.common.con_login import *
import json
import requests

# global  header 
# header=common_header(self)
# def get_dynamic_list_f_id(self):
#     header=common_header(self)
#     url = 'http://119.27.167.20:8083/dynamic/lists.json'
#     re = requests.get(url,headers=header)
#     dynamic_id = re.json()['data']['data'][0]['_id']
#     return dynamic_id
# def get_user_dynamic_f_id(self):
#     header=common_header(self)
#     url = 'http://119.27.167.20:8083/member/dynamiclists.json'
#     re = requests.get(url, headers = header)
#     user_dynamic_id = re.json()['data']['data'][0]['_id']
#     return user_dynamic_id
# def get_user_demand_id(self):
#     header=common_header(self)
#     url = 'http://119.27.167.20:8083/demand/otherList.json'
#     re = requests.get(url, headers = header)
#     user_demand_id = re.json()['data']['data'][0]['_id']
#     return user_demand_id
def  get_record_id():
    header = common_header_web()
    url = "http://111.204.225.50:8113/d225-8085/zhl-qiaokao/api/note/notebook/getnoterecordlist"
    data = {"op_path":"note.notebook.getnoterecordlist",
"grade_id":"11",
"subject_id":"2",
"private_tags":[],
"source":[],
"system_tags":[],
"page_no":0,
"page_size":10,
"phrase":"3",
"practice_time_order":1,
"type":2,
"business_id":"100001"}
    data2=json.dumps(data)
    # print(type(data2))


    re = requests.post(url, headers=header, data=data2)
    # print(re.request.body)

    # print(re.text)
    id = re.json()['data']['word_list'][0]['record_id']
    # print(type(id))
    # print(id)
    return {'record_ids':[id]}

