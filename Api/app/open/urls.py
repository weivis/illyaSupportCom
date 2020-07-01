from app.open import open, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@open.route('/index', methods=["POST"])
@requestPOST
def index(request):
    '''
    '''
    c,m,d = views.index(request.json)
    return ReturnRequest(c,m,d)