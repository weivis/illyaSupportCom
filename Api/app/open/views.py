from app.Extensions import db
from app.Models.db_Account import AccountUser
from app.Models.db_Video import VideoData
from app.Models.db_Bangumi import BangumiAnime
from app.Config import SERVER_GULAOBURL
from app.Models.db_Photo import PhotoData
from app.Models.db_Article import ArticleData

def index(request):

    madamv = [{
        'author_head': SERVER_GULAOBURL + '/static/com/userhead/' + AccountUser.query.filter_by(id=int(i.upload_userid)).first().head if AccountUser.query.filter_by(id=int(i.upload_userid)).first().head else SERVER_GULAOBURL + '/static/com/userhead/' + 'default.png',
        'author_username': AccountUser.query.filter_by(id=i.upload_userid).first().username,
        'id':i.id,
        # 'upload_userid':i.upload_userid,
        # 'verify_type':i.verify_type,
        # 'verify_falseinfo':i.verify_falseinfo,
        # 'classification':i.classification,
        # 'content_classification':i.content_classification,
        # 'identification':i.identification,
        'title':i.title,
        'cover':SERVER_GULAOBURL + "/static/com/video/cover/" + i.cover,
        # 'introduce':i.introduce,
        'source_type':i.source_type,
        'original_type':i.original_type,
        # 'original_url':i.original_url,
        # 'original_author':i.original_author,
        # 'videoloadurl':i.videoloadurl,
        # 'show_index':i.show_index,
        'create_time':i.create_time.strftime("%Y-%m-%d %H:%M:%S")
    } for i in VideoData.query.filter_by(verify_type=1).order_by(VideoData.create_time.desc()).limit(4)]
    
    bangumi = [{
        'id':i.id,
        'classification':i.classification,
        'identification':i.identification,
        'name':i.name,
        'setscount':i.setscount,
        'introduce':i.introduce,
        'cover':SERVER_GULAOBURL + '/static/com/bangumi/cover/' + i.cover,
        'upstatus':i.upstatus,
        # 'staff':i.staff,
        'status':i.status,
        'station_play':i.station_play,
        'openplay_time':i.openplay_time.strftime("%Y-%m-%d"),
        'sort':i.sort
    } for i in BangumiAnime.query.filter_by(status=1).order_by(BangumiAnime.sort.desc()).limit(4)]

    photo = [{
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
    } for i in PhotoData.query.filter_by(verify=1).order_by(PhotoData.create_time.desc()).limit(6)]

    news = [{
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
    }for i in ArticleData.query.filter_by(status=1).order_by(ArticleData.sort.desc()).limit(2)]

    return 200, '', {
        'madamv': madamv,
        'bangumi': bangumi,
        'photo': photo,
        'news': news
    }