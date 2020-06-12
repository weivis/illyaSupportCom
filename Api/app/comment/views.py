from app.Extensions import db
from app.Models.db_Comment import CommentMain, CommentReport
from app.Tool import _Paginate
from app.Models.db_Account import AccountUser

def comment_list(request):
    masterid = request.get('masterid', None)
    commentid = request.get('commentid', None)
    pages = request.get('pages', 1)

    if not masterid or not commentid:
        return 400, '参数有误', {}

    if masterid:
        data = CommentMain.query.filter(CommentMain.masterid == masterid, CommentMain.comment_type == 1, CommentMain.is_delete == False).order_by( BangumiAnime.create_time.desc())
    
    if commentid:
        data = CommentMain.query.filter(CommentMain.mainid == commentid, CommentMain.comment_type == 2, CommentMain.is_delete == False).order_by( BangumiAnime.create_time.desc())
    
    count, items, page, pages = _Paginate(data, pages)

    result = [{
        'senduser_name':AccountUser.query.filter_by(id=i.senduser_id).first().username,
        'senduser_head':AccountUser.query.filter_by(id=i.senduser_id).first().head if AccountUser.query.filter_by(id=i.senduser_id).first().head else '',
        'content':i.content,
        'time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")

    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }

# def comment_sublist(request):
#     commentid = request.get('commentid', None)
#     pages = request.get('pages', 1)
#     data = CommentMain.query.filter(CommentMain.mainid == commentid, CommentMain.comment_type == 2, CommentMain.is_delete == False).order_by( BangumiAnime.create_time.desc())

#     count, items, page, pages = _Paginate(data, pages)

#     result = [{
#         'senduser_name':AccountUser.query.filter_by(id=i.senduser_id).first().username,
#         'senduser_head':AccountUser.query.filter_by(id=i.senduser_id).first().head if AccountUser.query.filter_by(id=i.senduser_id).first().head else '',
#         'content':i.content,
#         'time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")
#     }for i in items]

#     return 200, 'ok', {
#         'result':result, 'count':count, 'page':page, 'pages':pages
#     }

def comment_send(request):
    current_account = request['current_account']

    masterid = request.get('masterid', None) 
    content = request.get('content', None)
    commentid = request.get('commentid', None)
    reply_commentid = request.get('reply_commentid', None)

    if not content:
        return 400, '内容不能为空', {}

    if not masterid or not commentid:
        return 400, '参数有误', {}

    add = CommentMain()
    add.senduser_id = current_account.id
    add.content = content
    if masterid:
        add.comment_type = 1
    else:
        add.comment_type = 2
        add.mainid = commentid
        add.reply_comment_id = reply_commentid

    try:
        db.session.add(add)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def comment_report(request):
    current_account = request['current_account']
    commentid = request.get('commentid', None)

    if not CommentMain.query.filter_by(id = commentid).first():
        return 400, '举报的评论不存在', {}

    add = CommentReport()
    add.report_comment_id = commentid
    add.userid = current_account.id

    try:
        db.session.add(add)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}