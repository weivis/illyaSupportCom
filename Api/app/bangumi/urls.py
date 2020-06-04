from app.bangumi import bangumi, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@bangumi.route('/sign-in', methods=["POST"])
@requestPOST
def bangumi_list(request):
    '''番剧列表
    Args

    Result
    '''
    c,m,d = views.bangumi_list(request.json)
    return ReturnRequest(c,m,d)