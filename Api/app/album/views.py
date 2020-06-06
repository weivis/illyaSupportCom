from app.Models.db_Album import AlbumData, AlbumDowurl
from app.Models.db_Bangumi import BangumiAnime
from app.Common import Generate_identification

def album_list(request):
    types = request.get('types', 0)
    pages = request.get('pages', 1)
    sfilter = request.get('sfilter', 0)

    if sfilter == 0:
        data = AlbumData.query.filter_by(status=1).order_by(
            AlbumData.create_time.desc(),
            AlbumData.sort.desc()
            )
    else:
        data = AlbumData.query.filter().order_by(
            AlbumData.create_time.desc(),
            AlbumData.sort.desc()
            )

    if types != 0:
        data = data.filter_by(classification=types)

    count, items, page, pages = _Paginate(data, pages)

    result = [{
        'id':i.id,
        'classification':i.classification,
        'identification':i.identification,
        'name':i.name,
        'cover':i.cover,
        'introduce':i.introduce,
        'status':i.status,
        'show_index':i.show_index,
        'relation_bangumi_id':i.relation_bangumi_id,
    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }

def album_info(request):
    id = request.get('id',None)
    if not id:
        return 400, 'id不能为空', {}

    i = AlbumData.query.filter_by(id=id)
    if not i:
        return 401, '资源不存在', {}

    result = {
        'id':i.id,
        'classification':i.classification,
        'identification':i.identification,
        'name':i.name,
        'cover':i.cover,
        'introduce':i.introduce,
        'status':i.status,
        'show_index':i.show_index,
        'relation_bangumi_id':i.relation_bangumi_id,
    }

    if i.relation_bangumi_id:
        relation_bangumidata = BangumiAnime.query.filter_by(id=i.relation_bangumi_id).first()
        if relation_bangumidata:
            relation_bangumi = {
                'id':relation_bangumidata.id,
                'name':relation_bangumidata.name,
                'cover':relation_bangumidata.cover
            }
    else:
        relation_bangumi = {}

    return 200, 'ok', {
        'result':result, 'relation_bangumi':relation_bangumi
    }

def album_add_or_edit(request):
    id = request.get('id',None)
    name = request.get('name',None)
    cover = request.get('cover',None)
    introduce = request.get('introduce',None)
    relation_bangumi_id = request.get('relation_bangumi_id',None)

    if not name:
        return 400, '资源名不能为空', {}

    if not cover:
        return 400, '封面不能为空', {}

    if not introduce:
        return 400, '介绍不能为空', {}

    if relation_bangumi_id:
        if not BangumiAnime.query.filter_by(id=relation_bangumi_id).first():
            return 400, '关联的番剧不存在', {}

    if id:
        obj = AlbumData.query.filter_by(id=id).first()

        if not obj:
            return 400, '编辑对象不存在或id错误', {}

    else:
        obj = AlbumData()

    obj.classification = classification
    obj.name = name
    obj.cover = cover
    obj.introduce = introduce
    obj.status = 2
    obj.show_index = False
    obj.relation_bangumi_id = int(relation_bangumi_id)

    try:
        if not id:
            obj.identification = Generate_identification('bangumi')
            db.session.add(obj)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def album_change(request):
    id = request.get('id',None)

    if not id:
        return 400, '资源id不存在', {}

    changeto = request.get('changeto',None)

    if not changeto:
        return 400, '操作不能为空', {}

    obj = AlbumData.query.filter(Article.id == id).first()

    if not obj:
        return 400, '资源不存在', {}

    if changeto == 1:
        if obj.status == 1:
            obj.status = 2
        else:
            obj.status = 1

    if changeto == 2:
        if obj.show_index == False:
            obj.show_index = True
        else:
            obj.show_index = False

    if changeto == 3:
        if obj.is_delete == False:
            obj.is_delete = True
        else:
            obj.is_delete = False

    try:
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def album_dowurl_list(request):
    id = request.get('id',None)

    if not id:
        return 400, '资源id不存在', {}

    album = AlbumData.query.filter_by(id=id).first()
    if not album:
        return 400, '资源不存在或资源id有误', {}

    data = AlbumDowurl.query.filter_by(album_id=id).all()

    result = [{
        'id':i.id,
        'dowsource_name':i.dowsource_name,
        'name':i.name,
        'dowinfo':i.dowinfo,
        'feedback':i.feedback
    }for i in data]

    return 200, 'ok', result

def album_dowurl_add_or_edit(request):
    id = request.get('id',None)
    album_id = request.get('album_id',None)
    dowsource_name = request.get('dowsource_name',None)
    name = request.get('name',None)
    dowinfo = request.get('dowinfo',None)

    if not album_id:
        return 400, '所属资源id不能为空', {} 

    if not dowsource_name:
        return 400, '来源名不能为空', {} 

    if not name:
        return 400, '资源名不能为空', {} 

    if not dowinfo:
        return 400, '下载信息不能为空', {} 

    if not AlbumData.query.filter_by(id=album_id).first():
        return 400, '所属资源不存在或id有误', {}

    if id:
        obj = AlbumDowurl.query.filter_by(id=id).first()

        if not obj:
            return 400, '编辑对象不存在或id错误', {}

    else:
        obj = AlbumDowurl()

    obj.album_id = album_id
    obj.dowsource_name = dowsource_name
    obj.name = name
    obj.dowinfo = dowinfo

    try:
        if not id:
            db.session.add(obj)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def album_dowurl_del(request):
    id = request.get('id',None)

    if not id:
        return 400, '资源id不存在', {}

    obj = AlbumDowurl.query.filter_by(id=id).first()
    if not obj:
        return 400, '数据不存在或id有误', {}

    try:
        db.session.delete(obj)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        return 502, '服务器出错', {}

def album_dowurl_feedback(request):
    id = request.get('id',None)

    if not id:
        return 400, '资源id不存在', {}

    obj = AlbumDowurl.query.filter_by(id=id).first()

    if not obj:
        return 400, '数据不存在或id有误', {}

    obj.feedback = int(obj.feedback) + 1

    try:
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def album_dowurl_change(request):
    id = request.get('id',None)
    dowinfo = request.get('dowinfo',None)

    if not id:
        return 400, '资源id不存在', {}

    obj = AlbumDowurl.query.filter_by(id=id).first()

    if not obj:
        return 400, '数据不存在或id有误', {}

    obj.feedback = 0

    if dowinfo:
        obj.dowinfo = dowinfo
    else:
        obj.dowinfo = str(obj.dowinfo)

    try:
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}