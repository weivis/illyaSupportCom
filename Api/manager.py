# -*- coding: utf-8 -*-
import os
from app import create_app, Config
from app.Extensions import db
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server, Command
from app.Models import db_Account
from app.Models.db_Account import AccountAdmin
from flask_bcrypt import generate_password_hash

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

# 输入赋值
@manager.option('-em', '-email', dest='email')
@manager.option('-pw', '-password', dest='password')
@manager.option('-un', '-username', dest='username')

# python manager.py create_admin -em 1@qq.com -pw 123456 -un WeiVi
def create_admin(email ,password, username):
    if not all([email, password, username]):
        print('参数不齐全')

    else:
        add = AccountAdmin()
        add.email = email
        add.password = generate_password_hash(password)
        add.username = username
        db.session.add(add)

        try:
            db.session.commit()
            print('成功创建管理员 : ', add)
            print('登录账号:',email)
            print('登录密码:',password)

        except Exception as e:
            print(e)
            db.session.rollback()
            print('添加管理员失败')


manager.add_command('db',MigrateCommand)
manager.add_command("runserver", Server(host=Config.RUNHOST, port=Config.RUNPORT, use_debugger=Config.USEFLASKDEBUG))

if __name__ == '__main__':
    manager.run()
