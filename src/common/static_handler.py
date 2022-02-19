import os
from flask import Blueprint, send_from_directory, send_file
# static_folder = os.path.join(os.path.dirname(__file__), '../../../front/build')
static_folder = os.path.join(os.path.dirname(__file__), '../../../front/build')

bp = Blueprint('static', __name__, url_prefix='/', static_folder=static_folder)


# static_folder = os.path.join(os.path.dirname(__file__), '../../front/build')
# static_folder = os.path.join(os.path.dirname(__file__), '../../../../front/build')
# print(static_folder)


@bp.route('/', methods=['GET'])
def index():
    print('INDEX')
    print(bp.static_folder)
    return bp.send_static_file('index.html')
    # return send_from_directory(os.path.join(os.path.dirname(__file__), '../../../front/build'), 'index.html')

