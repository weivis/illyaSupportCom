from app.Models.db_Article import ArticleData
from app.Common import Generate_identification
from app.Tool import _Paginate
from app.Extensions import db
from app.Config import SERVER_GULAOBURL

def article_list(request):
    print(request)
    types = request.get('types', 0)
    pages = request.get('pages', 1)
    sfilter = request.get('sfilter', 0)

    if sfilter == 0:
        data = ArticleData.query.filter(
            ArticleData.is_delete==False,
            ArticleData.status==1
            ).order_by(
            ArticleData.create_time.desc(),
            ArticleData.sort.desc()
            )
    else:
        data = ArticleData.query.filter().order_by(
            ArticleData.create_time.desc(),
            ArticleData.sort.desc()
            )

    if types != 0:
        data = data.filter_by(classification=types)

    count, items, page, pages = _Paginate(data, pages)

    result = [{
        'id':i.id,
        'classification':i.classification,
        'identification':i.identification,
        'title':i.title,
        'cover':SERVER_GULAOBURL + '/static/com/article/cover/' + i.cover,
        'introduce':i.introduce,
        'sort':i.sort,
        'status':i.status,
        'show_index':i.show_index,
        'is_delete':i.is_delete
    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }

def article_info(request):
    id = request.get('id',None)
    if not id:
        return 400, 'id不能为空', {}

    i = ArticleData.query.filter_by(id=id).first()
    if not i:
        return 401, '文章不存在', {}

    result = {
        'id':i.id,
        'classification':i.classification,
        'identification':i.identification,
        'title':i.title,
        'cover':SERVER_GULAOBURL + '/static/com/article/cover/' + i.cover,
        'file':i.cover,
        'introduce':i.introduce,
        'sort':i.sort,
        'status':i.status,
        'show_index':i.show_index,
        'is_delete':i.is_delete,
        'content':i.content,
        'create_time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    return 200, 'ok', result

def article_addoredit(request):
    print(request)
    id = request.get('id',None)
    classification = request.get('classification',None)
    title = request.get('title',None)
    cover = request.get('cover',None)
    introduce = request.get('introduce',None)
    content = request.get('content',None)

    if id:
        obj = ArticleData.query.filter_by(id=id).first()

        if not obj:
            return 400, '文章不存在', {}
    else:
        obj = ArticleData()

    if classification not in [1,2] or not classification:
        return 400, '文章类型有误', {}

    if not title:
        return 400, '文章标题不能为空', {}

    if not cover:
        return 400, '封面不能为空', {}

    if not introduce:
        return 400, '介绍不能为空', {}

    if not content:
        return 400, '内容不能为空', {}

    obj.classification = classification
    obj.title = title
    obj.cover = cover
    obj.introduce = introduce
    obj.content = content

    if not id:
        obj.status = 2 # 默认状态是下架
        obj.sort = 0 # 默认权重是0

    try:
        if not id:
            obj.identification = Generate_identification('article')
            db.session.add(obj)

        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def article_change(request):
    id = request.get('id',None)

    if not id:
        return 400, '文章不存在', {}

    changeto = request.get('changeto',None)

    if not changeto:
        return 400, '操作不能为空', {}

    obj = ArticleData.query.filter(ArticleData.id == id).first()

    if not obj:
        return 400, '文章不存在', {}

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

    if changeto == 4:
        sort = request.get('sort',None)
        if not sort:
            return 400, '新的权重值不能为空 最小值为0', {}
        obj.sort = sort

    if changeto == 5:
        db.session.delete(obj)

    try:
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}
