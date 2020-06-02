from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@user.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})