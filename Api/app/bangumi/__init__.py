from flask import Blueprint
bangumi = Blueprint('bangumi', __name__)
from ..bangumi import urls