from flask import Blueprint
from src.models.Aircraft import Aircraft
atran = Blueprint('atran', __name__, url_prefix='/atran')


@atran.route('/dow', methods=['get'])
def post_ofp():
    # acft = Aircraft()
    # acft.oew = 99999
    # acft.tail = 'rere'
    # acft.water = 333
    # acft.save()
    # print(ofp_handlers.ofp)
    acfts = Aircraft.objects().to_json()
    # print(acfts)
    return acfts
    # return 'ok'