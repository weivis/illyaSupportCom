from app.Extensions import db
from datetime import datetime

# CV表
class CvData(db.Model):
    
    __tablename__ = 'cv_data'
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(255))         # 人名
    head = db.Column(db.String(255))                # 头像
    isdelete = db.Column(db.Boolean, default=False) # 删除
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间