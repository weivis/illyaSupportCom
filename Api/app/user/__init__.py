from flask import Blueprint
user = Blueprint('user', __name__)
from ..user import urls