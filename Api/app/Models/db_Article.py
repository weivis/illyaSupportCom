from app.Extensions import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

# 文章表
class ArticleData(db.Model):
    
    __tablename__ = 'article_data'

    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.Integer)          # 分类
    '''
        1 = 官方资讯
        2 = 手办
    '''
    title = db.Column(db.String(255))               # 标题
    cover = db.Column(db.String(255))               # 封面图
    introduce = db.Column(db.String(255))           # 简介
    content = db.Column(LONGTEXT)                   # 文章内容
    status = db.Column(db.Integer)                  # 上下架状态
    '''
        1 = 正常
        2 = 下架
    '''
    show_index = db.Column(db.Boolean, default=False) # 首页展示
    is_delete = db.Column(db.Boolean, default=False) # 是否删除
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间