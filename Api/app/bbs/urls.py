from app.bbs import bbs, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@bbs.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})