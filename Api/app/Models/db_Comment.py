from app.Extensions import db
from datetime import datetime

# 主评论表
class CommentMain(db.Model):
    
    __tablename__ = 'comment_main'

    id = db.Column(db.Integer, primary_key=True)
    masterid = db.Column(db.String(255))            # 唯一值 用做评论标识
    senduser_id = db.Column(db.Integer)             # 发送用户id
    comment_type = db.Column(db.Integer)            # 评论类型              1 主评论 2 子评论
    content = db.Column(db.Text)                    # 内容
    mainid = db.Column(db.Integer)                  # 主评论id
    reply_comment_id = db.Column(db.Integer)        # 回复评论id
    is_delete = db.Column(db.Boolean, default=False)# 是否被删除
    deleteinfo = db.Column(db.String(255))          # 删除原因
    subcomment_type = db.Column(db.Boolean, default=False) # 是否存在二级评论
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    '''
        获取某个key的评论列表:
        masterid = 唯一值
        comment_type = 1
        排序 = create_time

        获取某个主评论下的子评论
        mainid = 主评论id
        comment_type = 2
        排序 = create_time
    '''

# 评论举报表
class CommentReport(db.Model):
    
    __tablename__ = 'comment_report'

    id = db.Column(db.Integer, primary_key=True)
    report_comment_id = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)  # 更新时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间