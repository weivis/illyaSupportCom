from app.admin import admin
from app.album import album
from app.bangumi import bangumi
from app.article import article
from app.auth import auth
from app.bbs import bbs
from app.user import user
from app.video import video
from app.cv import cv
from app.open import open
from app.comment import comment

DEFAULT_BLUEPRINT = (
    (admin, '/admin'),
    (album, '/album'),
    (bangumi, '/bangumi'),
    (article, '/article'),
    (auth, '/auth'),
    (bbs, '/bbs'),
    (user, '/user'),
    (video, '/video'),
    (cv, '/cv'),
    (open, '/open'),
    (comment, '/comment')
)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix = '/api' + prefix)