import redis

redis_io0 = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

# 验证码模块 ------------------------------------------------------------------------------------------

from app.Tool import RandomStr

def CreateVcode(code_type, data):
    try:
        time = (60 * 20)
        key = str(code_type) + RandomStr()
        redis_io0.setex(str(key), time, str(data))
        return True, key

    except Exception as e:
        print(e)
        return False, None

def CheckVcode(key):
    try:
        data = redis_io0.get(str(key))

        if data:
            try:
                redis_io0.delete(str(key))
            except Exception as e:
                print(e)
            return data
        return False

    except Exception as e:
        print(e)

# # 用户身份鉴定---------------------------------------------------------------------------------------

# def RedisSigninUser(token, userid):
#     try:
#         time = (60 * 10)
#         print(token, userid, time)
#         redis_io0.setex(str(token), time, str(userid))
#         return True

#     except Exception as e:
#         print(e)
#         return False

# def RedisAuthUser(token):
#     user = redis_io0.get(str(token))
#     if user:
#         return user
#     return False

# def RedisLogout(token):
#     redis_io0.delete(str(token))
#     return True