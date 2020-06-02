from app.video import video, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@video.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})