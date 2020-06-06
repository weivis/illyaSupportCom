from app.Extensions import db
from datetime import datetime

# 视频表
class VideoData(db.Model):

    __tablename__ = 'video_data'
    id = db.Column(db.Integer, primary_key=True)
    upload_userid = db.Column(db.Integer)               # 上传者用户id
    verify_type = db.Column(db.Integer)                 # 审核状态
    '''
        1 审核通过
        2 审核不合格退回
    '''
    verify_falseinfo = db.Column(db.String(255))        # 审核不通过的原因
    classification = db.Column(db.Integer)              # 视频分类
    '''
        1   MAD·AMV
        2   MMD
        3   技术宅
        4   其他
        10  pv
    '''
    content_classification = db.Column(db.Integer)      # 视频内容分类
    '''
        1 静止系
        2 剪辑向
        3 混合向
    '''
    identification = db.Column(db.String(255))          # 唯一身份标识
    title = db.Column(db.String(255))                   # 视频标题
    cover = db.Column(db.Text)                          # 封面
    introduce = db.Column(db.Text)                      # 介绍
    upload_type = db.Column(db.Integer)                 # 投稿类型
    '''
        1 原创
        2 转载
    '''
    videoloadurl = db.Column(db.Text)                   # 视频加载地址
    original_url = db.Column(db.String(255))            # 转载地址
    original_author = db.Column(db.String(255))         # 原作者名称
    show_index = db.Column(db.Boolean, default=False)   # 首页展示
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间