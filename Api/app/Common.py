from flask import jsonify

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