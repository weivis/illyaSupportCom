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