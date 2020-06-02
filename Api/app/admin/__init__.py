from flask import Blueprint
admin = Blueprint('admin', __name__)
from ..admin import urls