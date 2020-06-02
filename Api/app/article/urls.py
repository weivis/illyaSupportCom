from app.article import article, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@article.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})