import os

from flask import Blueprint, send_from_directory

bp = Blueprint('static', __name__, url_prefix='/')

static_folder = os.path.join(os.path.dirname(__file__), '../../../front/build')


@bp.route('/', methods=['GET'])
def index():
    return send_from_directory(static_folder, 'index.html')
