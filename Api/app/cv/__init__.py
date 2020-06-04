from flask import Blueprint
cv = Blueprint('cv', __name__)
from ..cv import urls