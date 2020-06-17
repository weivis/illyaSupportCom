from app.bangumi import bangumi, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@bangumi.route('/list', methods=["POST"])
@requestPOST
def bangumi_list(request):
    '''番剧列表
    Args
        types(int) 获取的资源类型
            1 = 番剧
            2 = 剧场版
            3 = OVA
            4 = SP
        pages(int) 分页 默认1
        sfilter(int) 默认0 0正常 1全部

    Result
        code:   状态码
        msg:    消息
        data:
            result
                id              id
                name            番剧名
                setscount       剧集总数
                introduce       介绍
                cover           封面
                upstatus        连载状态
                staff           staff制作信息
                station_play    是否支持站内播放
                openplay_time   开播时间
                sort            权重
            count   总搜索结果条数
            page    当前页数
            pages   总页数
    '''
    c,m,d = views.bangumi_list(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/info', methods=["POST"])
@requestPOST
def bangumi_info(request):
    '''获取详细番剧信息
    Args
        id
    Result
        code:   状态码
        msg:    消息
        data:
            result
                id
                name
                setscount
                introduce
                cover
                upstatus
                staff
                station_play
                openplay_time
                sort
            playsource
                id
                url
                source_name
                bangumi_id
                sort
    '''
    c,m,d = views.bangumi_info(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/add_or_edit', methods=["POST"])
@requestPOST
def bangumi_add_or_edit(request):
    '''添加番剧或编辑
    Args
        classification(int)类型
            1 = 番剧
            2 = 剧场版
            3 = OVA
            4 = SP
        openplay_time(str)开播日期 格式yyyy-MM-dd
        name(str)番剧名
        setscount(int)总集数
        introduce(str)介绍
        cover(str)封面
        upstatus(int)连载状态 1 = 连载中 2 = 已完结
        staff(str)制作信息
        station_play(int)1 = 运行 2 = 不允许
        status(int)上下架状态 1 正常 2 = 下架
        sort(int)权重

    Result
        code:   状态码
            200 成功
        msg:    消息
        data:   null
    '''
    c,m,d = views.bangumi_add_and_edit(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/change', methods=["POST"])
@requestPOST
def bangumi_change(request):
    '''更改番剧(删除 上下架)
    Args
        status(int)修改上下架状态 1 正常 2 下架
        dele(all)不为空代表删除

    Result
        code:   状态码
            200 成功
        msg:    消息
        data:   null
    '''
    c,m,d = views.bangumi_change(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/playurl/addoredit', methods=["POST"])
@requestPOST
def bangumi_playurl_add_or_edit(request):
    '''添加播放源地址和编辑
    Args
        id              int     id
        url             str     地址
        source_name     str     资源地址名字
        bangumi_id      int     番剧id
        sort            int     权重值

    Result
        code:   状态码
            200 成功
        msg:    消息
        data:   null
    '''
    c,m,d = views.bangumi_playurl_addoredit(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/playurl/del', methods=["POST"])
@requestPOST
def bangumi_playurl_del(request):
    '''删除播放源地址
    Args
        id              int     id

    Result
        code:   状态码
            200 成功
        msg:    消息
        data:   null
    '''
    c,m,d = views.bangumi_playurl_del(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/cv/addoredit', methods=["POST"])
@requestPOST
def Bangumi_cv_addoredit(request):
    '''绑定cv和编辑已经绑定了的cv
    Args
        id                      int     id
        bangumi_id              int     番剧id
        cv_id                   int     cvid
        sort                    int     权重
        role_name               str     角色名

    Result
        code:   状态码
            200 成功
        msg:    消息
        data:   null
    '''
    c,m,d = views.Bangumi_cv_addoredit(request.json)
    return ReturnRequest(c,m,d)

@bangumi.route('/cv/del', methods=["POST"])
@requestPOST
def Bangumi_cv_del(request):
    '''删除单个绑定了的CV配音信息
    Args
        id                      int     id

    Result
        code:   状态码
            200 成功
        msg:    消息
        data:   null
    '''
    c,m,d = views.Bangumi_cv_del(request.json)
    return ReturnRequest(c,m,d)