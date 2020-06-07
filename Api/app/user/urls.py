from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@user.route('/get/userinfo', methods=["POST"])
@requestPOST
def get_userinfo(request):
    '''获取用户信息
    Args
        {
            id:id
        }
    Result
        code:   状态码
        msg:    消息
        data:
            email
            head
            username
            create_time
            msg_remind
            newreply_count
            introduce
    '''
    c,m,d = views.get_userinfo(request.json)
    return ReturnRequest(c,m,d)

@user.route('/myinfo', methods=["POST"])
@TokenPost([2])
def user_info(request):
    '''获取用户信息
    Args
        {}
    Result
        code:   状态码
        msg:    消息
        data:
            email
            head
            username
            create_time
            msg_remind
            newreply_count
            introduce
    '''
    c,m,d = views.user_info(request.json)
    return ReturnRequest(c,m,d)

@user.route('/edit-myinfo', methods=["POST"])
@TokenPost([2])
def user_editinfo(request):
    '''编辑用户信息
    不需要更改的参数可以不传
    Args
        head        str         头像
        username    str         用户名
        introduce   str         个人介绍
    Result
        code:   状态码
        msg:    消息
        data:
    '''
    c,m,d = views.user_editinfo(request.json)
    return ReturnRequest(c,m,d)