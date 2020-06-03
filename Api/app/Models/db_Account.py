from app.Extensions import db
from datetime import datetime

# 管理员表
class AccountAdmin(db.Model):
    
    __tablename__ = 'account_admin'
    id = db.Column(db.Integer, primary_key=True)

    token = db.Column(db.Text)
    email = db.Column(db.Text)
    head = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

# 用户表
class AccountUser(db.Model):
    
    __tablename__ = 'account_user'
    id = db.Column(db.Integer, primary_key=True)

    token = db.Column(db.Text)
    email = db.Column(db.Text)
    head = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)
    '''
        0 = 未进行邮箱验证
        1 = 正常用户
        2 = 受限用户
        3 = 禁止登录
    '''
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    msg_remind = db.Column(db.Boolean)
    newreply_count = db.Column(db.Integer)