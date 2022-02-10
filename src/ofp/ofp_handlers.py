from flask import Blueprint, request

ofp = Blueprint('ofp', __name__, url_prefix='/ofp')


@ofp.route('', methods=['POST'])
def post_ofp():
    print(request.json)
    return 'Ok'
