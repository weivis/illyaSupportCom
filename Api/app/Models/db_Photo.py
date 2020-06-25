from app.Extensions import db
from datetime import datetime

# 相册表
class PhotoData(db.Model):
    
    __tablename__ = 'photo_data'
    id = db.Column(db.Integer, primary_key=True)    # id
    upload_user = db.Column(db.Integer)             # 上传用户
    file = db.Column(db.Text)                       # 文件
    title = db.Column(db.String(255))               # 标题
    info = db.Column(db.Text)                       # 介绍
    category = db.Column(db.Integer)                # 类目
    verify = db.Column(db.Integer)                  # 类目
    '''
        1 : 通过审核
        2 = 未审核
    '''
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间