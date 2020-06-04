from app.Models.db_Account import AccountUser
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib
from datetime import datetime
from app.Extensions import db
from app import Config
from app.Email import SeedEmail
from app.Redis import CreateVcode, CheckVcode
from app.Tool import CheckEmailStr

def auth_sign_in(request):
    email = request.get('email', None)
    password = request.get('password', None)

    if not email or not password:
        return 400, '账户或密码不正确', {}

    user = AccountUser.query.filter_by(email=email).first()
    if not user:
        return 400, '账户不存在', {}

    if user.status == 3:
        return 400, '该账户存在异常 请联系管理员', {}

    if user.status == 0:
        return 10001, '账户未通过邮箱验证 请先完成验证', {}

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
            return 200, '登录成功', dict(token=md5, username=user.username, head=head)

        except Exception as e:
            print(e)
            db.session.rollback()
            return 502, '服务器出错', {}

    return 400, '账户或密码不正确', {}


def auth_register(request):
    email = request.get('email', None)
    username = request.get('username', None)
    password = request.get('password', None)
    repassword = request.get('repassword', None)

    if not all([email, username, password, repassword]):
        return 400, '输入信息有误', {}

    if AccountUser.query.filter_by(username=username).first():
        return 400, '用户名已存在', {}

    if not CheckEmailStr(email):
        return 400, '邮箱格式有误', {}

    emailuser = AccountUser.query.filter_by(email=email).first()
    if emailuser:
        if emailuser.status == 0:
            return 10000, '账户未通过邮箱验证 请先完成验证', {}

    if AccountUser.query.filter_by(email=email).first():
        return 400, '邮箱已存在', {}

    if str(password) != str(repassword):
        return 400, '两次输入不一致', {}

    try:
        u = AccountUser()
        u.username = str(username)
        u.email = str(email)
        u.password = generate_password_hash(password)
        u.status = 0
        db.session.add(u)
        db.session.flush()

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
        return 200, '注册成功', {'vcode': vcode, 'email':email}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def auth_register_again_sendemail(request):
    email = request.get('email',None)

    querys = AccountUser.query.filter_by(email=email).first()
    if not querys:
        return 400, '该邮箱未注册', {}

    if querys.status != 0:
        return 400, '该邮箱以验证完成 无法重复发送注册验证码', {}

    gtype, vcode = CreateVcode('', {'id': querys.id})
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

    return 200, '以重新发送', {'email':email}
    

def auth_verify_register_vcode(request):
    vcode = request.get('vcode',None)

    if not vcode:
        return 400, '验证码有误', {}

    data = CheckVcode(vcode)
    if data:
        u = AccountUser.query.filter_by(id=data['id']).first()

        if u.status == 1:
            return 400, '已验证过无法重复验证', {} 

        try:
            u.status = 1
            db.session.commit()
            return 200, '验证成功', {}

        except Exception as e:
            print(e)
            db.session.rollback()
            return 502, '服务器出错', {}

    return 400, '验证码有误', {}

def auth_logout(request):
    current_account = request['current_account']
    current_account.token = ''

    try:
        db.session.commit()
        return 200, '退出成功', {}

    except:
        db.session.rollback()
        return 502, '服务器出错', {}