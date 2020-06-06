from app.Extensions import db
from datetime import datetime

# 资源表
class AlbumData(db.Model):
    
    __tablename__ = 'album_data'
    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.Integer)          # 资源分类
    identification = db.Column(db.String(255))      # 唯一身份标识
    '''
        1 = 番剧
        2 = OST
        3 = MMD
        4 = Live2D
    '''
    name = db.Column(db.Text)                       # 资源标题
    cover = db.Column(db.String(255))               # 封面图
    introduce = db.Column(db.Text)                  # 介绍
    status = db.Column(db.Integer)                  # 上下架状态
    '''
        1 = 正常
        2 = 下架
    '''
    show_index = db.Column(db.Boolean, default=False) # 首页展示
    relation_bangumi_id = db.Column(db.Integer)       # 关联番剧id
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

# 资源下载地址表
class AlbumDowurl(db.Model):
    
    __tablename__ = 'album_dowurl'
    id = db.Column(db.Integer, primary_key=True)
    dowsource_name = db.Column(db.String(255))               # 下载资源来源名
    name = db.Column(db.String(255))                         # 资源名
    dowinfo = db.Column(db.Text)                             # 下载信息
    feedback = db.Column(db.Integer,default=0)               # 反馈次数统计 管理员确认资源没问题后恢复0
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间