from app.Models.db_Video import VideoData
from app.Common import Generate_identification
from app.Tool import _Paginate
from app.Extensions import db
from app.Config import SERVER_GULAOBURL

def video_list(request):
    print(request)
    types = request.get('types', 0)
    pages = request.get('pages', 1)
    ctypes = request.get('ctypes', 0)
    sfilter = request.get('sfilter', 0)
    userid = request.get('userid', None)

    data = VideoData.query.filter().order_by(VideoData.create_time.desc())

    if userid:
        data = data.filter_by(upload_userid=int(userid))

    if sfilter == 0:
        data = data.filter_by()

    if sfilter == 1:
        data = data.filter_by(verify_type=1)

    if sfilter == 2:
        data = data.filter_by(verify_type=2)

    if sfilter == 3:
        data = data.filter_by(verify_type=3)

    if sfilter == 4:
        data = data.filter_by(verify_type=4)

    if types == 1:
        if ctypes != 0:
            data = data.filter_by(content_classification=types)

    if types != 0:
        data = data.filter_by(classification=types)

    count, items, page, pages = _Paginate(data, pages)

    result = [{
        'id':i.id,
        'upload_userid':i.upload_userid,
        'verify_type':i.verify_type,
        'verify_falseinfo':i.verify_falseinfo,
        'classification':i.classification,
        'content_classification':i.content_classification,
        'identification':i.identification,
        'title':i.title,
        'cover':SERVER_GULAOBURL + "/static/com/video/cover/" + i.cover,
        'introduce':i.introduce,
        'source_type':i.source_type,
        'original_type':i.original_type,
        'original_url':i.original_url,
        'original_author':i.original_author,
        'videoloadurl':i.videoloadurl,
        'show_index':i.show_index,
        # 'update_time':i.update_time.strftime("%Y-%m-%d"),
        'create_time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")
    }for i in items]

    return 200, 'ok', {
        'result':result, 'count':count, 'page':page, 'pages':pages
    }

def video_query(request):
    id = request.get('id', None)

    if not id:
        return 404, 'ID不能为空', {}

    obj = VideoData.query.filter_by(id=id).first()

    if not obj:
        return 400, '视频不存在', []
 
    i = obj

    return 200, "", {
        'id':i.id,
        'upload_userid':i.upload_userid,
        'verify_type':i.verify_type,
        'verify_falseinfo':i.verify_falseinfo,
        'classification':i.classification,
        'content_classification':i.content_classification if i.content_classification else 0,
        'identification':i.identification,
        'title':i.title,
        'cover':SERVER_GULAOBURL + "/static/com/video/cover/" + i.cover,
        'filecover': i.cover,
        'introduce':i.introduce,
        'source_type':i.source_type,
        'original_type':i.original_type,
        'original_url':i.original_url,
        'original_author':i.original_author,
        'videoloadurl':i.videoloadurl,
        'show_index':i.show_index,
        'create_time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")
    }

def video_upload_or_edit(request):
    current_account = request['current_account']
    id = request.get('id', None)
    classification = request.get('classification', None)
    content_classification = request.get('content_classification', None)
    title = request.get('title', None)
    cover = request.get('cover', None)
    introduce = request.get('introduce', None)
    source_type = request.get('source_type', None)
    original_type = request.get('original_type', None)
    original_url = request.get('original_url', None)
    original_author = request.get('original_author', None)
    videoloadurl = request.get('videoloadurl', None)

    if classification not in [1,2.3,4,10] or not classification:
        return 400, '视频分类有误', {}

    if classification == 1:
        if content_classification not in [1,2,3] or not content_classification:
            return 400, '视频内容分类有误', {}

    if not title:
        return 400, '视频标题有误', {} 

    if not cover:
        return 400, '必须上传封面', {} 

    if not introduce:
        return 400, '视频介绍不能为空', {} 

    if not source_type or source_type not in [1,2,10]:
        return 400, '来源类型有误', {} 

    if original_type not in [1,2] or not original_type:
        return 400, '投稿类型有误', {}

    if original_type == 2:
        if not original_url:
            return 400, '转载地址不能为空', {} 

        if not original_author:
            return 400, '原作者名不能为空', {} 

    if not videoloadurl:
        return 400, '投稿源视频地址不能为空', {}

    if id:
        add = VideoData.query.filter_by(id=id).first()
        if not add:
            return 400, '编辑的视频不存在', {}
    else:
        add = VideoData()

    if original_type == 2:
        add.original_type = original_type
        add.original_url = original_url

    add.content_classification = int(content_classification)
    add.classification = int(classification)
    add.original_type = original_type
    add.upload_userid = current_account.id
    add.verify_type = 2
    add.title = title
    add.cover = cover
    add.introduce = introduce
    add.source_type = source_type
    add.videoloadurl = videoloadurl

    try:
        if not id:
            add.identification = Generate_identification('video')
            db.session.add(add)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        db.session.rollback()
        return 502, '服务器出错', {}

def video_del(request):
    current_account = request['current_account']
    id = request.get('id', None)

    if not id:
        return 400, 'id不能为空', {}

    obj = VideoData.query.filter_by(id=id).first()

    if not obj:
        return 400, '视频不存在', {}

    if obj.upload_userid != current_account.id:
        return 400, '非法操作', {} 

    try:
        db.session.delete(obj)
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        return 502, '服务器出错', {}

def video_admin_verify(request):
    id = request.get('id', None)
    verify_type = request.get('verify_type', None)
    verify_falseinfo = request.get('verify_falseinfo', None)

    if not int(verify_type) or int(verify_type) not in [1,2,3,4]:
        return 400, '参数有误', {}

    if not id:
        return 400, 'id不能为空', {}

    if verify_type == 3 or verify_type == 4:
        if not verify_falseinfo:
            return 400, '退回理由不能为空', {}

    obj = VideoData.query.filter_by(id=id).first()

    if not obj:
        return 400, '视频不存在', {}

    obj.verify_type = int(verify_type)
    obj.verify_falseinfo = str(verify_falseinfo)

    try:
        db.session.commit()
        return 200, '', {}

    except Exception as e:
        print(e)
        return 502, '服务器出错', {}