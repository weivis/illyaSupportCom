from app.photo import photo, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@photo.route('/list', methods=["POST"])
@requestPOST
def photo_list(request):
    '''获取列表
    Args
        category    int     分区
            1 : 原创
            2 : Pixiv
            3 : Cospaly
        sfilter     int|str 内容类型
        userid      int     用户id
        pages       int     分页

    Result
        id
        upload_userid
        file
        title
        info
        category
        pixiv_author
        verify
        create_time
    '''
    c,m,d = views.list(request.json)
    return ReturnRequest(c,m,d)

@photo.route('/up', methods=["POST"])
@TokenPost([2])
def photo_up(request):
    '''上传图片
    Args
        file        str     文件
        title       str     标题
        info        str     介绍
        category    int     分区
            1 : 原创
            2 : Pixiv
            3 : Cospaly

    Result
        200 成功
    
    '''
    c,m,d = views.up(request.json)
    return ReturnRequest(c,m,d)

@photo.route('/change', methods=["POST"])
@requestPOST
def change(request):
    '''用户操作
    Args
        id      int       要操作的图片id
        set     int       操作类型
            1 : 删除

    Result
        code
            200 成功
            201 非法
            502 出错
    '''
    c,m,d = views.change(request.json)
    return ReturnRequest(c,m,d)

@photo.route('/admin/change', methods=["POST"])
@requestPOST
def admin_change(request):
    '''管理员操作
    Args
        id      int       要操作的图片id
        set     int       操作类型
            1 : 通过审核
            2 : 等待审核中
            3 : 未审核
            4 : 删除

    Result
        code
            200 成功
            201 图片对象不存在
            502 出错
    '''
    c,m,d = views.admin_change(request.json)
    return ReturnRequest(c,m,d)