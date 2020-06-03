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
        token(str)请求token
        username(str)用户名
        head(str)用户头像
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

    '''
    c,m,d = views.auth_register(request.json)
    return ReturnRequest(c,m,d)