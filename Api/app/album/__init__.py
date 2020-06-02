from flask import Blueprint
album = Blueprint('album', __name__)
from ..album import urls