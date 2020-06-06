from app.article import article, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@article.route('/list', methods=["POST"])
@requestPOST
def article_list(request):
    '''文章列表
    Args
        types(int) 获取的资源类型
            0 = 全部 默认
            1 = 官方资讯
            2 = 手办
        pages(int) 分页 默认1
        sfilter(int) 默认0 0正常 1全部

    Result
        code:   状态码
        msg:    消息
        data:   
            result  [
                id
                classification
                title
                cover
                introduce
                sort
                status
                show_index
                is_delete
            ]
            count   总搜索结果条数
            page    当前页数
            pages   总页数
    '''
    c,m,d = views.article_list(request.json)
    return ReturnRequest(c,m,d)

@article.route('/info', methods=["POST"])
@requestPOST
def article_info(request):
    '''文章信息
    Args
        id      int     文章id

    Result
        code:   状态码
        msg:    消息
        data:   
            id
            classification
            title
            cover
            introduce
            sort
            status
            show_index
            is_delete
            content

    '''
    c,m,d = views.article_info(request.json)
    return ReturnRequest(c,m,d)

@article.route('/addoredit', methods=["POST"])
@requestPOST
def article_addoredit(request):
    '''添加文章或编辑文章
    Args
        id                  int     文章id
        classification      int     文章分类
            1 = 官方资讯
            2 = 手办
        title               str     文章标题
        cover               str     封面
        introduce           str     介绍
        content             str     内容

    Result
        code:   状态码
        msg:    消息
        data:   

    '''
    c,m,d = views.article_addoredit(request.json)
    return ReturnRequest(c,m,d)

@article.route('/change', methods=["POST"])
@requestPOST
def article_change(request):
    '''更改文章状态和排序
    Args
        id          int     文章id
        changeto    int     更改类型
            1 上下架
            2 是否首页展示
            3 是否删除文章
            4 修改权重值
                sort    int     权重值

    Result
        code:   状态码
        msg:    消息
        data:   

    '''
    c,m,d = views.article_change(request.json)
    return ReturnRequest(c,m,d)