from app.admin import admin, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenPost

@admin.route('/', methods=["POST"])
@requestPOST
def test(request):
    return ReturnRequest(200, 'test', {})