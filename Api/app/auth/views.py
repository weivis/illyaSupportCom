from app.Models.db_Account import AccountUser
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib
from datetime import datetime
from app.Extensions import db
from app import Config
from app.Email import SeedEmail
from app.Redis import CreateVcode


def auth_sign_in(request):
    email = request.get('email', None)
    passport = request.get('passport', None)

    if not email or not passport:
        return 400, '账户或密码不正确', {}

    user = AccountUser.query.filter_by(email=email).first()
    if not user:
        return 400, '账户不存在', {}

    if user.status == 3:
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
                head = Config.SERVER_STATICLOADURL + \
                    '/user/head/' + str(user.head)
            return 200, '成功', dict(token=md5, username=user.username, head=head)

        except Exception as e:
            print(e)
            db.session.rollback()
            return 502, '服务器出错', {}

    return 400, '账户或密码不正确', {}


def Check_EmailStr(email):
    # re.compile(r"\"?([a-zA-Z0-9_-]+@\w+\.\w+)\"?")
    pattern = re.compile(r"\"?([0-9A-Za-z\-_\.]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


def auth_register(request):
    email = request.get('email', None)
    username = request.get('username', None)
    password = request.get('password', None)
    repassword = request.get('repassword', None)

    if not all([email, username, password, repassword]):
        return 201, '输入信息有误', {}

    if AccountUser.query.filter_by(username=username).first():
        return 203, '用户名已存在', {}

    if not Check_EmailStr(email):
        return 204, '邮箱格式有误', {}

    if AccountUser.query.filter_by(email=email).first():
        return 205, '邮箱已存在', {}

    if str(password) != str(repassword):
        return 206, '两次输入不一致', {}

        try:
            u = AccountUser()
            u.password = str(username)
            u.email = str(email)
            u.password = generate_password_hash(password)
            u.status = 0
            db.session.add(u)
            db.session.first()

            gtype, vcode = CreateVcode('', {'id': u.id})
            if gtype:

                try:
                    html = '<h3>点击以下链接完成账户注册验证</h3><a>{0}</a>'.format(
                        str(vcode))
                    SeedEmail(
                        email_title='[ 魔法少女伊莉雅应援站(illya-support.weivird.com) ]注册账户邮箱验证',
                        email_body='请点击链接完成账户注册验证',
                        email_html=html,
                        recipients=[email],
                        sender='happys_wei@163.com'
                    )

                except Exception as e:
                    print(e)
                    return 503, '服务器出错', {}

            else:
                return 504, '服务器出错', {}

            db.session.commit()

        except Exception as e:
            print(e)
            db.session.rollback()
            return 502, '服务器出错', {}

    return 200, '', {'vcode': vcode}


def auth_verify_register_vcode(request):
    return 200, '', {}


def auth_logout(request):
    return 200, '', {}
