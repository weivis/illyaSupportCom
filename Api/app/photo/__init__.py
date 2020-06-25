from flask import Blueprint
photo = Blueprint('photo', __name__)
from ..photo import urls