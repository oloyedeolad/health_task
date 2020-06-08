from flask import Blueprint

hmo = Blueprint('hmo', __name__)

from . import view