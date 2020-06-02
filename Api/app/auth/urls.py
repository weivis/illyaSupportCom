from app.auth import auth, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@auth.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})