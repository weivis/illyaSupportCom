from app.video import video, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@video.route('/list', methods=["POST"])
@requestPOST
def video_list(request):
    '''视频列表
    Args
        types       int     分类
            0   全部
            1   mad
            2   技术宅
            3   其他
            10  pv
        ctypes      int     子分类
            1 mad
                1   静止系
                2   剪辑向
                3   混合向
        pages       int     分页        默认为1
        sfilter     int     类型        默认为0
            0   正常 只有审核通过的视频
            1   全部
            2   等待审核
            3   审核不合格退回
            4   被管理员删除
        userid      int     用户id

    Result
        code:   状态码
        msg:    消息
        data:
            result[{
                id
                upload_userid
                verify_type
                verify_falseinfo
                classification
                content_classification
                identification
                title
                cover
                introduce
                source_type
                original_type
                original_url
                original_author
                videoloadurl
                show_index
                create_time
            }]
            count   总搜索结果条数
            page    当前页数
            pages   总页数
    '''
    c,m,d = views.video_list(request.json)
    return ReturnRequest(c,m,d)

@video.route('/uploadoredit', methods=["POST"])
@TokenPost([2])
def video_upload_or_edit(request):
    '''视频投稿和编辑
    Args
        id              int             视频id
        classification  int             视频分类
            1   MAD·AMV
            2   MMD
            3   技术宅
            4   其他
            10  pv
        content_classification int      视频内容分类
            1   静止系
            2   剪辑向
            3   混合向
        title           str             标题
        cover           str             封面
        introduce       str             介绍
        source_type     int             来源类型
            1   B站
            2   A站
            10  直传
        original_type   int             投稿类型
            1   原创
            2   转载
        original_url    str             转载地址
        original_author str             原作者名称
        videoloadurl    str             videoloadurl

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_upload_or_edit(request.json)
    return ReturnRequest(c,m,d)

@video.route('/user/del', methods=["POST"])
@requestPOST
def video_del(request):
    '''用户删除视频
    Args
        id              int             视频id
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_del(request.json)
    return ReturnRequest(c,m,d)

@video.route('/admin/change', methods=["POST"])
@requestPOST
def video_admin_verify(request):
    '''管理员操作视频
    Args
        id                  int             视频id
        verify_type         int             审核类型
            1 审核通过
            2 等待审核
            3 审核不合格退回
        verify_falseinfo    str             退回原因

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.video_admin_verify(request.json)
    return ReturnRequest(c,m,d)