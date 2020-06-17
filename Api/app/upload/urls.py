from app.upload import upload, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

# 上传文件
@upload.route('/', methods=["POST"])
@requestPOST
def upload_file(request):
    '''统一上传接口
        参数
            file : file
            uploadKey : 上传的key值(问后端要 不同的上传文件 调用的地方 用的key值都不一样)
        return
            ospath : 系统内的储存位置 如: /static/xxx.jpg
            lodpath : 可加载地址 如 http:www.xxx.com/static/xxx.jpg
            filename 统一数据库储存该字段
        code
            200 ok
            400 错误: 没有文件
                错误: Key值不能为空
                文件类型不允许
                错误: 不允许使用的Key值
        
    '''
    c,m,d = views.upload_file(request)
    return ReturnRequest(c,m,d)