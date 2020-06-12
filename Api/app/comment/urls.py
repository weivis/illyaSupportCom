from app.comment import comment, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@comment.route('/list', methods=["POST"])
@requestPOST
def comment_list(request):
    '''评论列表
    Args
        masterid        str         评论主key
        commentid       int         主评论id 用于获取二级评论
        pages           int         页数 默认1
    Result
        code:
        msg:
        data:[
            {
                senduser_name
                senduser_head
                content
                time
            }
        ]
    '''
    c,m,d = views.comment_list(request.json)
    return ReturnRequest(c,m,d)

# @comment.route('/sublist', methods=["POST"])
# @requestPOST
# def comment_sublist(request):
#     '''二级评论列表
#     Args
#     Result
#     '''
#     c,m,d = views.comment_sublist(request.json)
#     return ReturnRequest(c,m,d)

@comment.route('/send', methods=["POST"])
@TokenPost([2])
def comment_send(request):
    '''发送评论
    Args
        masterid            唯一key
        commentid           主评论id
        content             内容
        reply_commentid     回复的评论的id
    Result
        code:
        msg:
        data:
    '''
    c,m,d = views.comment_send(request.json)
    return ReturnRequest(c,m,d)

@comment.route('/report', methods=["POST"])
@requestPOST
def comment_report(request):
    '''评论举报
    Args
        commentid
    Result
        200
    '''
    c,m,d = views.comment_report(request.json)
    return ReturnRequest(c,m,d)