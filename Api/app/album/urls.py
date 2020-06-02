from app.album import album, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@album.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})