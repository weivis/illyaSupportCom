from app.Models.db_Bangumi import BangumiAnime, BangumiPlayurl
from app.Tool import _Paginate, StrForDate
from app.Extensions import db

def bangumi_list(request):
    types = request.get('types', 0)
    pages = request.get('pages', 1)
    sfilter = request.get('sfilter', 0)

    if sfilter == 0:
        data = BangumiAnime.query.filter_by(status=1).order_by(
            BangumiAnime.create_time.desc(),
            BangumiAnime.sort.desc()
            )
    else:
        data = BangumiAnime.query.filter().order_by(
            BangumiAnime.create_time.desc(),
            BangumiAnime.sort.desc()
            )

    if types:
        data = data.filter_by(classification=types)

    count, items, page, pages = _Paginate(data, pages)

    result = [{
        'id':i.id,
        'name':i.name,
        'setscount':i.setscount,
        'introduce':i.introduce,
        'cover':i.cover,
        'upstatus':i.upstatus,
        'staff':i.staff,
        'station_play':i.station_play,
        'openplay_time':i.openplay_time.strftime("%Y-%m-%d"),
        'sort':i.sort
    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }

def bangumi_info(request):
    id = request.get('id',None)
    if not id:
        return 400, 'id不能为空', {}

    i = BangumiAnime.query.filter_by(id=id)
    if not i:
        return 401, '番剧不存在', {}

    result = {
        'id':i.id,
        'name':i.name,
        'setscount':i.setscount,
        'introduce':i.introduce,
        'cover':i.cover,
        'upstatus':i.upstatus,
        'staff':i.staff,
        'station_play':i.station_play,
        'openplay_time':i.openplay_time.strftime("%Y-%m-%d"),
        'sort':i.sort
    }

    playsourcedata = BangumiPlayurl.query.filter_by(bangumi_id=i.id).order_by(BangumiPlayurl.sort.desc()).all()

    playsource = [{
        'id':i.id,
        'url':i.url,
        'source_name':i.source_name,
        'bangumi_id':i.bangumi_id,
        'sort':i.sort
    } for i in playsourcedata]

    return 200, 'ok', {
        'result':result, 'playsource':playsource
    }

def bangumi_add_and_edit(request):
    id = request.get('id',None)
    classification = request.get('classification',None)
    openplay_time = request.get('openplay_time',None)
    name = request.get('name',None)
    setscount = request.get('setscount',None)
    introduce = request.get('introduce',None)
    cover = request.get('cover',None)
    upstatus = request.get('upstatus',None)
    staff = request.get('staff',None)
    station_play = request.get('station_play',None)
    status = request.get('status',None)
    sort = request.get('sort',None)

    if not id:
        obj = BangumiAnime()

    if id:
        obj = BangumiAnime.query.filter_by(id=id).first()
        if not obj:
            return 400, '编辑的番剧不存在', {}

    if not classification:
        return 400, '番剧分类不能为空', {}

    if not name:
        return 400, '番剧名不能为空', {}

    if not setscount:
        return 400, '剧集数不能为空或为0', {}

    if not introduce:
        return 400, '介绍不能为空', {}

    if not cover:
        return 400, '封面不能为空', {}

    if not upstatus:
        return 400, '连载状态不能为空', {}
    upstatus = {1:True, 2:False}[int(upstatus)]

    if not station_play:
        return 400, '是否允许站内播放', {}
    station_play = {1:True, 2:False}[int(station_play)]

    if not status:
        return 400, '上下架状态不能为空', {}

    if not sort:
        sort = 0

    openplay_time = StrForDate(openplay_time)
    if not openplay_time:
        return 400, '日期格式有误yyyy-MM-dd', {}

    obj.classification = classification
    obj.openplay_time = openplay_time
    obj.name = name
    obj.setscount = setscount
    obj.introduce = introduce
    obj.cover = cover
    obj.upstatus = upstatus
    obj.staff = staff
    obj.station_play = station_play
    obj.status = status
    obj.sort = sort

    try:
        if not id:
            db.session.add(obj)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def bangumi_change(request):
    pass

def bangumi_playurl_add(request):
    pass

def bangumi_playurl_edit(request):
    pass

def bangumi_playurl_del(request):
    pass