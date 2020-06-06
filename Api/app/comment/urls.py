from app.comment import comment, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@comment.route('/list', methods=["POST"])
@requestPOST
def comment_list(request):
    '''评论列表
    Args
    Result
    '''
    c,m,d = views.comment_list(request.json)
    return ReturnRequest(c,m,d)

@comment.route('/send', methods=["POST"])
@requestPOST
def comment_send(request):
    '''发送评论
    Args
    Result
    '''
    c,m,d = views.comment_send(request.json)
    return ReturnRequest(c,m,d)

@comment.route('/report', methods=["POST"])
@requestPOST
def comment_report(request):
    '''评论举报
    Args
    Result
    '''
    c,m,d = views.comment_report(request.json)
    return ReturnRequest(c,m,d)