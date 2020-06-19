from app.album import album, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@album.route('/list', methods=["POST"])
@requestPOST
def album_list(request):
    '''资源列表
    Args
        types(int) 获取的资源类型
            1 = 番剧
            2 = OST
            3 = MMD
            4 = Live2D
        pages(int) 分页 默认1
        sfilter(int) 默认0 0正常 1全部

    Result
        code:   状态码
        msg:    消息
        data:
            result
                id
                classification
                identification
                name
                cover
                introduce
                status
                show_index
                relation_bangumi_id
            count   总搜索结果条数
            page    当前页数
            pages   总页数
    '''
    c,m,d = views.album_list(request.json)
    return ReturnRequest(c,m,d)

@album.route('/info', methods=["POST"])
@requestPOST
def album_info(request):
    '''资源详细信息
    Args
        id      int     资源id
    Result
        code:   状态码
        msg:    消息
        data:
            result
                id
                classification
                identification
                name
                cover
                introduce
                status
                show_index
                relation_bangumi_id

            relation_bangumi
                id
                name
                cover
    '''
    c,m,d = views.album_info(request.json)
    return ReturnRequest(c,m,d)

@album.route('/addoredit', methods=["POST"])
@requestPOST
def album_add_or_edit(request):
    '''添加资源和编辑资源
    Args
        id                      int     编辑的资源id
        classification          int     资源分类
        name                    str     资源名
        cover                   str     封面
        introduce               str     资源介绍
        relation_bangumi_id     int     关联的番剧id

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_add_or_edit(request.json)
    return ReturnRequest(c,m,d)

@album.route('/change', methods=["POST"])
@requestPOST
def album_change(request):
    '''更改资源状态
    Args
        id          int     资源id
        changeto    int     操作
            1 上下架
            2 是否首页展示
            3 是否删除
            4 物理删除
            5 取消绑定
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_change(request.json)
    return ReturnRequest(c,m,d)

@album.route('/bind/bangumi', methods=["POST"])
@requestPOST
def album_bind_bangumi(request):
    '''绑定番剧
    Args
        id          int     资源id
        bangumiid   int     番剧id
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_bind_bangumi(request.json)
    return ReturnRequest(c,m,d)

@album.route('/dowurl/list', methods=["POST"])
@requestPOST
def album_dowurl_list(request):
    '''获取资源的下载列表
    Args
        id      int        所属资源id

    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_dowurl_list(request.json)
    return ReturnRequest(c,m,d)

@album.route('/dowurl/addoredit', methods=["POST"])
@requestPOST
def album_dowurl_add_or_edit(request):
    '''新增资源下载地址和编辑
    Args
        id              int         编辑的id
        album_id        int         所属资源id
        dowsource_name  str         下载来源名字
        name            str         资源名
        dowinfo         str         下载信息
        
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_dowurl_add_or_edit(request.json)
    return ReturnRequest(c,m,d)

@album.route('/dowurl/del', methods=["POST"])
@requestPOST
def album_dowurl_del(request):
    '''删除资源下载列表的某一项
    Args
        id      int     要删除的数据的id
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_dowurl_del(request.json)
    return ReturnRequest(c,m,d)

@album.route('/dowurl/feedback', methods=["POST"])
@requestPOST
def album_dowurl_feedback(request):
    '''反馈资源下载问题
    Args
        id      int     反馈的资源id
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_dowurl_feedback(request.json)
    return ReturnRequest(c,m,d)

@album.route('/dowurl/feedback', methods=["POST"])
@requestPOST
def album_dowurl_change(request):
    '''更改资源下载的反馈状态
    Args
        id          int     反馈的资源id
        dowinfo     str     下载信息
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.album_dowurl_change(request.json)
    return ReturnRequest(c,m,d)