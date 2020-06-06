from app.video import video, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@video.route('/list', methods=["POST"])
@requestPOST
def video_list(request):
    '''视频列表
    Args
        types       int     分类
            1   mad
            2   技术宅
            3   其他
            10  pv
        pages       int     分页        默认为1
        sfilter     int     类型        默认为0, 0=正常，1=全部

    Result
        code:   状态码
        msg:    消息
        data:
            result
            count   总搜索结果条数
            page    当前页数
            pages   总页数
    '''
    c,m,d = views.video_list(request.json)
    return ReturnRequest(c,m,d)

@video.route('/upload', methods=["POST"])
@requestPOST
def video_upload(request):
    '''视频投稿
    Args

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_upload(request.json)
    return ReturnRequest(c,m,d)

@video.route('/edit', methods=["POST"])
@requestPOST
def video_edit(request):
    '''视频编辑
    Args

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_edit(request.json)
    return ReturnRequest(c,m,d)

@video.route('/user/change', methods=["POST"])
@requestPOST
def video_user_change(request):
    '''用户操作视频
    Args

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_user_change(request.json)
    return ReturnRequest(c,m,d)

@video.route('/admin/change', methods=["POST"])
@requestPOST
def video_admin_change(request):
    '''管理员操作视频
    Args

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_admin_change(request.json)
    return ReturnRequest(c,m,d)

@video.route('/admin/verify', methods=["POST"])
@requestPOST
def video_admin_verify(request):
    '''管理员审核视频
    Args

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_admin_verify(request.json)
    return ReturnRequest(c,m,d)