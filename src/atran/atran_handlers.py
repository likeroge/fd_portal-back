from src.models.Aircraft import Aircraft
from flask import Blueprint, request, jsonify
atran = Blueprint('atran', __name__, url_prefix='/atran')


@atran.route('/dow', methods=['get'])
def post_ofp():
    acfts  = Aircraft.objects().to_json()
    return acfts
