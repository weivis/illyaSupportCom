import redis

redis_io0 = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

# 验证码模块 ------------------------------------------------------------------------------------------

from app.Tool import RandomStr

def CreateVcode(code_type, data):
    '''创建基于Redis的验证码
    Args
        code_type(str)验证码类型 如 [注册, 登录, 下载]
        data(dict)验证码所携带的数据

    Result
        True，返回数据
        False，无效
    '''
    try:
        time = (60 * 20)
        if code_type or code_type != '':
            key = str(code_type) + '-' + RandomStr()
        else:
            key = RandomStr()
        redis_io0.setex(str(key), time, str(data))
        return True, key

    except Exception as e:
        print(e)
        return False, None

def CheckVcode(key):
    '''验证码检验
    Args
        key(str)验证码

    Result
        data(dict) 返回的是字典代表验证码正确 返回的是Flase就是验证码不存在或错误
    '''
    try:
        data = redis_io0.get(str(key))

        if data:
            try:
                redis_io0.delete(str(key))
            except Exception as e:
                print(e)
            return eval(data)
        return False

    except Exception as e:
        print(e)