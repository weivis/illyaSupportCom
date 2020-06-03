from functools import wraps
from flask import request
from app.Common import ReturnRequest

from app.Models.db_Account import AccountAdmin, AccountUser

def requestPOST(func=None):
    '''
        [POST]通用Post请求
        条件: POST
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest(405,'请求方法不对','')
    return wrapper

def TokenPost(user_group):
    '''
        @TokenPost
        Args
            Token(headers.str)用户Token
            user_group(args.int)允许访问的用户类型, 1 管理员, 2 普通用户
        Returns
            current_account = request['current_account']
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method == 'POST':

                token = request.headers.get('Token', None)
                auth = Auth(token, user_group)

                if auth.status():
                    request.json['current_account'] = auth.account
                    return func(request, *args, **kwargs )

                else:
                    c,m,d = auth.errormsg()
                    return ReturnRequest(c,m,d)

            else:
                return ReturnRequest(405,'请求方法不正确','',{})
        return wrapper
    return decorator

class Auth:
    
    def __init__(self, token, user_group):

        Adminclass = AccountAdmin
        Userclass = AccountUser

        if 1 in user_group:
            self.account = Adminclass.query.filter(Adminclass.token == token).first()

        if 2 in user_group:
            self.account = Userclass.query.filter(Userclass.token == token).first()

        self.token = token
        self.user_group = user_group
        self.ret_data = {}
        self.ret_cnmsg = ''
        self.ret_code = 10086
        if not user_group:
            print('注意！@UserTokenAuthPost: 未设置可访问的用户权限')

    def status(self):
        if not self.token:
            self.ret_cnmsg = '非法请求'
            self.ret_code = 10086
            return False

        if not self.account:
            self.ret_cnmsg = 'Token已失效或不正确, 请重新登录'
            self.ret_code = SystemCode.TokenInvalid
            return False

        return True

    def account(self):
        return self.account

    def errormsg(self):
        return self.ret_code, self.ret_cnmsg, self.ret_data
