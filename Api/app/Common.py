from flask import jsonify
from app.Tool import RandomStr
import time

def ReturnRequest(code, msg, data):
    '''
        统一返回请求的处理结果
    '''
    if not msg:
        msg = '成功'
    jso = {'code':code, 'msg': msg,'data': data}

    # 打印每个请求的返回结果
    # print('Return : ' + str(code) + ' => ' + str(jso))
    return jsonify(jso)

def Generate_identification(material):
    '''
        生成数据的唯一标识
    '''
    t = int(time.time())
    return str(RandomStr() + str(material) + str(t))