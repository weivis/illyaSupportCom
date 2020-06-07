from app.Models.db_Account import AccountUser

def get_userinfo(request):
    id = request.get('id', None)

    if not id:
        return 400, '用户不存在', {}
        
    user = AccountUser.query.filter_by(id=id).first()
    
    if not user:
        return 400, '用户不存在', {}
    
    return 200, '', {
        'email':user.email,
        'head':user.head,
        'username':user.username,
        'create_time':user.create_time.strftime("%Y-%m-%d"),
        'msg_remind':user.msg_remind,
        'newreply_count':user.newreply_count,
        'introduce':user.introduce
    }

def user_info(request):
    current_account = request['current_account']
    user = AccountUser.query.filter_by(id=current_account.id).first()
    return 200, '', {
        'email':user.email,
        'head':user.head,
        'username':user.username,
        'create_time':user.create_time.strftime("%Y-%m-%d"),
        'msg_remind':user.msg_remind,
        'newreply_count':user.newreply_count,
        'introduce':user.introduce
    }

def user_editinfo(request):
    current_account = request['current_account']
    head = request.get('head', None)
    username = request.get('username', None)
    introduce = request.get('introduce', None)

    user = AccountUser.query.filter_by(id=current_account.id).first()

    if head:
        user.head = head

    if username:
        user.username = username

    if introduce:
        user.introduce = introduce

    try:
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}