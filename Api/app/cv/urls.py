from app.cv import cv, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@cv.route('/list', methods=["POST"])
@requestPOST
def cv_list(request):
    '''CV列表
    Args
        keyword(str)搜索
        sfilter(int)过滤器 0 正常 ,1 全部
    Result
        id, people_name, head
        {
        "code": 200,
        "data": [
            {
            "head": "0.png",
            "id": 1,
            "people_name": "唯酱"
            }
        ],
        "msg": "成功"
        }
    '''
    c,m,d = views.cv_list(request.json)
    return ReturnRequest(c,m,d)

@cv.route('/add', methods=["POST"])
@requestPOST
def cv_add(request):
    '''CV添加
    Args
        people_name 人名
        head        头像
    Result
        200 成功
    '''
    c,m,d = views.cv_add_or_edit(request.json)
    return ReturnRequest(c,m,d)

@cv.route('/edit', methods=["POST"])
@requestPOST
def cv_edit(request):
    '''CV编辑
    Args
        id          要编辑的cvid
        people_name 人名
        head        头像
    Result
        200 成功
    '''
    c,m,d = views.cv_add_or_edit(request.json)
    return ReturnRequest(c,m,d)

@cv.route('/del', methods=["POST"])
@requestPOST
def cv_del(request):
    '''CV编辑
    Args
        id 要删除的cv的id
    Result
        200 成功
    '''
    c,m,d = views.cv_del(request.json)
    return ReturnRequest(c,m,d)