from app.Extensions import db
from datetime import datetime

# 番剧表
class BangumiAnime(db.Model):
    
    __tablename__ = 'bangumi_anime'
    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.Integer)      # 视频分类
    '''
        1 = 番剧
        2 = 剧场版
        3 = OVA
        4 = SP
    '''
    name = db.Column(db.String(255))            # 番剧名
    setscount = db.Column(db.Integer)           # 集数
    introduce = db.Column(db.Text)              # 介绍
    cover = db.Column(db.Text)                  # 封面
    upstatus = db.Column(db.Boolean)            # 连载状态 True 连载中 False 以完结
    staff = db.Column(db.Text)                  # STAFF内容
    station_play = db.Column(db.Boolean)        # 是否支持站内播放
    openplay_time = db.Column(db.DateTime)      # 开播时间
    status = db.Column(db.Integer)              # 状态
    '''
        1 = 正常
        2 = 下架
    '''
    sort = db.Column(db.Integer, default=0)                # 权重
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

# 番剧播放地址表
class BangumiPlayurl(db.Model):
    
    __tablename__ = 'bangumi_playurl'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))             # url
    source_name = db.Column(db.String(255))     # 来源名字
    bangumi_id = db.Column(db.Integer)          # 番剧id
    sort = db.Column(db.Integer)                # 权重
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

# 角色CV
class BangumiRolecv(db.Model):
    
    __tablename__ = 'bangumi_rolecv'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255))       # 角色名
    bangumi_id = db.Column(db.Integer)          # 所属番剧id
    cv_id = db.Column(db.Integer)               # cv_id
    sort = db.Column(db.Integer)                # 权重
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

# 番剧视频表
class BangumiVideo(db.Model):
    
    __tablename__ = 'bangumi_video'
    id = db.Column(db.Integer, primary_key=True)
    bangumi_id = db.Column(db.Integer)                 # 所属番剧id
    playsource_url = db.Column(db.String(255))         # 播放源地址
    title = db.Column(db.String(255))                  # 集标题
    sort = db.Column(db.Integer)                       # 集数
    cover = db.Column(db.Text)                         # 封面
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间