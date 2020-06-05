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
        
    Result
        code:   状态码
        msg:    消息
        data:
            result
                id      id
                
            count   总搜索结果条数
            page    当前页数
            pages   总页数
    '''
    c,m,d = views.bangumi_list(request.json)
    return ReturnRequest(c,m,d)