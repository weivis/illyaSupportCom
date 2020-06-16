from flask import Blueprint
upload = Blueprint('upload', __name__)
from ..upload import urls

