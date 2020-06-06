from app.open import open, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@open.route('/list', methods=["POST"])
@requestPOST
def cv_list(request):
    '''
    Args
    Result
    '''
    c,m,d = views.cv_list(request.json)
    return ReturnRequest(c,m,d)