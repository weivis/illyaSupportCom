from app.Models.db_Account import AccountUser
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib
from datetime import datetime
from app.Extensions import db
from app import Config

def auth_sign_in(request):
    email = request.get('email', None)
    passport = request.get('passport', None)

    if not email or not passport:
        return 400, '账户或密码不正确', {}

    user = AccountUser.query.filter_by(email=email).first()
    if not user:
        return 400, '账户不存在', {}

    if user.status != 0:
        return 400, '该账户存在异常 请联系管理员', {}

    if check_password_hash(str(user.password), str(password)):
        md5content = user.email + datetime.now().strftime("%Y%m%d%H%M%S")
        md5 = hashlib.md5(md5content.encode()).hexdigest()

        try:
            user.token = str(md5)
            db.session.commit()
            if not user.head or user.head == '':
                head = Config.SERVER_STATICLOADURL + '/user/head/' + 'default.png'
            else:
                head = Config.SERVER_STATICLOADURL + '/user/head/' + str(user.head)
            return 200, '成功', dict(token=md5, username=user.username, head=head)

        except Exception as e:
            print(e)
            connect.rollback()
            return 502, '服务器出错', {}

    return 400, '账户或密码不正确', {} 

def auth_register(request):
    return 200, '', {}

def auth_verify_register_vcode(request):
    return 200, '', {}

def auth_logout(request):
    return 200, '', {}