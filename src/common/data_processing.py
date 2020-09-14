



def _to_gbk(data):
    data1 = data.encode('gbk')

    return data1

def _to_utf8(data):
    data1 = data.encode('utf-8')
    return data1
def gbk_tozhongwen(data):
    data = data.encode('gbk').decode('gbk')
    return data
def utf8_tozhongwen(data):
    data = data.encode('utf-8').decode('utf-8')
    return data

