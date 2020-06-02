from flask import Blueprint
article = Blueprint('article', __name__)
from ..article import urls