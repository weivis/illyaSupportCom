from app.photo import photo, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@photo.route('/list', methods=["POST"])
@requestPOST
def cv_list(request):
    '''相簿列表
    Args

    Result
    
    '''
    c,m,d = views.list(request.json)
    return ReturnRequest(c,m,d)