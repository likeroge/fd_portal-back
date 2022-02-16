from flask import Blueprint, request, jsonify

from src.models.Aircraft import Aircraft

atran = Blueprint('atran', __name__, url_prefix='/atran')


@atran.route('/dow', methods=['get'])
def post_ofp():
    acfts  = Aircraft.objects().to_json()
    return acfts
