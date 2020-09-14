
import xlrd

def excel_to_list(data_file,sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)#sheet对象
    header = sh.row_values(0)##文件第0行
    for i in range(1,sh.nrows):
        d = dict(zip(header,sh.row_values(i)))##映射函数创建字典
        data_list.append(d)
    return data_list
def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:#查找用例
            return case_data
# @get_test_data()
# def get_test_data2(data_list,case_name):
#     url='http://111.204.225.50:8113/d225-8085/zhl-qiaokao'
#     url2='https://zhl-education.xxfz.com.cn'
#     for case_data in data_list:
#         if case_name == case_data['case_name']:
#             if url in case_data['url']:
#                 case_data['url'].split(,'api')
#             return case_data



if __name__=='__main__':
    data_list = excel_to_list("test_data.xlsx","TestUserLogin")
    # case_data = get_test_data(data_list, 'test_capcth_login')
    # print(case_data)
    # print(data_list)
    # print(type(data_list))
       
        
