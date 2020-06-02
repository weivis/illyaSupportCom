from app.anime import anime, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@anime.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})