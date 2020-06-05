from app.Models.db_Bangumi import BangumiAnime
from app.Tool import _Paginate

def bangumi_list(request):
    types = request.get('types', 0)
    pages = request.get('pages', 1)
    sfilter = request.get('sfilter', 0)

    if sfilter == 0:
        data = BangumiAnime.query.filter_by(status=0).order_by(BangumiAnime.create_time.desc())
    else:
        data = BangumiAnime.query.filter().order_by(BangumiAnime.create_time.desc())

    if types:
        data = data.filter_by(classification=types)

    count, items, page, pages = _Paginate(data, pages)

    result = [{
        'id':i.id
    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }
