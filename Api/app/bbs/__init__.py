from flask import Blueprint
bbs = Blueprint('bbs', __name__)
from ..bbs import urls