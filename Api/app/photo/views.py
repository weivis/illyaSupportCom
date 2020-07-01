from app.Extensions import db
from app.Models.db_Photo import PhotoData
from app.Config import SERVER_GULAOBURL
from app.Tool import _Paginate
from app.Models.db_Account import AccountUser
from app.Common import Generate_identification

def list(request):
    category = request.get('category', None)
    sfilter = request.get('sfilter', None)
    userid = request.get('userid', None)
    types = request.get('type', None)
    pages = request.get('pages', 1)

    if pages == 0:
        pages = 1

    # 创建搜索集
    if not sfilter:
        querys = PhotoData.query.filter(PhotoData.verify == 1)
    else:
        querys = PhotoData.query.filter()

    # 审核状态
    if types == 1:
        querys = querys.filter_by(verify=2)

    # 审核状态
    if types == 2:
        querys = querys.filter_by(verify=1)

    # 类目
    if category:
        querys = querys.filter(PhotoData.category == category)

    # 用户id
    if userid:
        querys = querys.filter_by(upload_user=int(userid))

    count, items, page, pages = _Paginate(querys, pages)

    result = [{
        'id':i.id,
        'upload_userid':i.upload_user,
        'file': SERVER_GULAOBURL + '/static/com/photo/image/' + i.file,
        'cover': SERVER_GULAOBURL + '/static/com/photo/cover/' + i.file,
        'title':i.title,
        'info':i.info,
        'category':i.category,
        'pixiv_author':i.pixiv_author,
        'verify':i.verify,
        'create_time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")
    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }

def up(request):
    current_account = request['current_account']
    files = request.get('file', None)
    title = request.get('title', None)
    info = request.get('info', None)
    category = request.get('category', None)

    if not files:
        return 201, '文件不能为空', {}

    if not title:
        return 201, '标题不能为空', {}

    if not category:
        return 201, '上传分区不能为空', {}

    if category == 2:
        pixiv_author = request.get('pixiv_author', None)

        if not pixiv_author:
            return 201, 'pixive图片作者不能为空', {}

    add = PhotoData()
    add.upload_user = current_account.id
    add.category = category
    add.title = title
    add.info = info
    add.file = files
    add.verify = 2

    try:
        add.identification = Generate_identification('Photo')
        db.session.add(add)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def change(request):
    current_account = request['current_account']
    id = request.get('id', None)
    sets = request.get('set', None)

    obj = PhotoData.query.filter_by(id=id).first()

    if not obj:
        return 201, '图片对象不存在', {}

    if sets:
        sets = int(sets)
        # 1
        if sets == 1:
            if obj.upload_user != current_account.id:
                return 201, '非法操作', {}
            try:
                db.session.delete(obj)
                db.session.commit()
                return 200, '', {}

            except Exception as e:
                print(e)
                return 502, '服务器出错', {}

    return 400, '操作类型不能为空', {}

def admin_change(request):
    print(request)
    id = request.get('id', None)
    sets = request.get('set', None)

    obj = PhotoData.query.filter_by(id=id).first()

    if not obj:
        return 201, '图片对象不存在', {}

    if sets:
        sets = int(sets)
        if sets == 1:
            obj.verify = 1

        if sets == 2:
            obj.verify = 3

        if sets == 3:
            db.session.delete(obj)

        try:
            db.session.commit()
            return 200, '成功', {}

        except Exception as e:
            print(e)
            return 502, '服务器出错', {}

    return 400, '操作类型不能为空或参数有误', {}