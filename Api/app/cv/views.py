from app.Models.db_Cv import CvData
from app.Extensions import db

def cv_list(request):
    keyword = request.get('keyword', None)
    sfilter = request.get('sfilter', 0)

    querys = CvData.query.filter()
    
    if sfilter == 1:
        querys = querys.filter(CvData.isdelete == False)

    if keyword:
        querys = querys.filter(CvData.people_name.contains(str(keyword)))

    result = [
        {
            'people_name':i.people_name,
            'head':i.head,

        } for i in querys.all()
    ]

    return 200, '', result

def cv_add_or_edit(request):
    people_name = request.get('people_name', None)
    head = request.get('head', None)

    if not all([people_name, head]):
        return 400, '参数缺失', {}

    add = CvData()
    add.people_name = str(people_name)
    add.head = str(head)

    try:
        db.session.add(add)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def cv_del(request):
    pass