from app.auth import auth, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@auth.route('/sign-in', methods=["POST"])
@requestPOST
def auth_sign_in(request):
    '''登录
    Args
        email(str)登录邮箱
        passport(str)登录密码

    Result
        200
            token(str)请求token
            username(str)用户名
            head(str)用户头像
        400
            账户或密码不正确
        401
            账户不存在
    '''
    c,m,d = views.auth_sign_in(request.json)
    return ReturnRequest(c,m,d)

@auth.route('/register', methods=["POST"])
@requestPOST
def auth_register(request):
    '''注册
    Args
        email(str)注册邮箱
        passport(str)登录密码
        repassport(str)重复输入一次密码

    Result
        200 
            成功
        400 
            邮箱已存在
            密码不一致
            密码或邮箱输入有误
    '''
    c,m,d = views.auth_register(request.json)
    return ReturnRequest(c,m,d)

@auth.route('/verify/register-vcode', methods=["POST"])
@requestPOST
def auth_verify_register_vcode(request):
    '''验证注册验证码
    Args
        code(str)验证码
    Result
        200
    '''
    c,m,d = views.auth_verify_register_vcode(request.json)
    return ReturnRequest(c,m,d)

@auth.route('/logout', methods=["POST"])
@TokenPost([1,2])
def auth_logout(request):
    '''退出登录
    Args
        null
    Result
        200
    '''
    c,m,d = views.auth_logout(request.json)
    return ReturnRequest(c,m,d)