from app.Models.db_Cv import CvData
from app.Extensions import db

def cv_list(request):
    keyword = request.get('keyword', None)
    sfilter = request.get('sfilter', 0)

    if sfilter == 0:
        querys = CvData.query.filter(CvData.isdelete == False).all()

    else:
        querys = CvData.query.filter().all()

    if keyword:
        querys = querys.filter(CvData.people_name.contains(str(keyword)))

    result = [
        {
            'id':i.id,
            'people_name':i.people_name,
            'head':i.head
        } for i in querys
    ]

    return 200, '', result

def cv_add_or_edit(request):
    id = request.get('id', None)
    people_name = request.get('people_name', None)
    head = request.get('head', None)

    if not all([people_name, head]):
        return 400, '参数缺失', {}

    if id:
        add = CvData.query.filter_by(id=id).first()

    else:
        add = CvData()

    if not add:
        return 400, '被编辑的CVid不存在', {} 

    add.people_name = str(people_name)
    add.head = str(head)

    try:
        if not id:
            db.session.add(add)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def cv_del(request):
    id = request.get('id', None)

    if not id:
        return 400, '参数缺失', {}
    
    obj = CvData.query.filter_by(id=id).first()

    if not obj:
        return 400, '对象不存在或id有误', {}

    try:
        obj.isdelete = True
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}