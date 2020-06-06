# 跨域密钥
SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

# DBUG
USEFLASKDEBUG = True

# ----------------------------------------------------------------------

# 测试服数据库
SQLALCHEMY_DATABASE_URI = "mysql://root:weivimysql@47.94.153.68:3306/illya_support?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/illya_support?charset=utf8mb4"

# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False

# ----------------------------------------------------------------------

# 服务器地址
HOSTQUERYTYPE = 'http'  # 协议
RUNHOST = '127.0.0.1'   # 运行ip
RUNPORT = 8080          # 运行端口号

SERVER_GULAOBURL = HOSTQUERYTYPE + '://' + RUNHOST + ':' + str(RUNPORT)

# 静态文件加载地址
SERVER_STATICLOADURL = SERVER_GULAOBURL + '/static'
# ----------------------------------------------------------------------

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'happys_wei@163.com'
MAIL_PASSWORD = 'YTKPXXRKISOTASSV'

# ----------------------------------------------------------------------

# CELERY_REDISDB = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL = CELERY_REDISDB

# ----------------------------------------------------------------------

API_DOC_MEMBER = ['api/comment','api/open','api/cv','api/admin','api/album','api/bangumi','api/auth','api/bbs','api/article','api/user','api/video','Api接口文档说明']

# 需要排除的 RESTful Api 文档
RESTFUL_API_DOC_EXCLUDE = []