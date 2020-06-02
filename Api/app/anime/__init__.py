from flask import Blueprint
anime = Blueprint('anime', __name__)
from ..anime import urls