from flask import Blueprint, request, jsonify
from src.models.Aircraft import Aircraft
from mongoengine.errors import DoesNotExist


aircraft = Blueprint('aircraft', __name__, url_prefix='/aircraft')


@aircraft.route('/find', methods=['get'])
def find_aircraft():
    argument_tail = request.args['tail']
    tail = argument_tail.upper()

    try:
        acft = Aircraft.objects.get(tail=tail).to_json()
        return acft
    except Exception as e:
        print('Not found', e)
        return jsonify({
            'water': 'ВС не найдено',
            'fak': 'ВС не найдено',
            'oew': 'ВС не найдено'
        })


@aircraft.route('/atran-state', methods=['POST'])
def save_all_acft_state():
    aircraft_state = request.get_json()['data']
    print(aircraft_state[-1])
    for acft in aircraft_state:
        acft_in_db = Aircraft.objects.get(tail=acft['tail'])
        # if acft_in_db['tail'] == 'TESTTEST':
        acft_in_db['fak'] = acft['fak']
        acft_in_db['oew'] = acft['oew']
        acft_in_db['crew'] = acft['crew']
        acft_in_db['is_water_on_board'] = acft['is_water_on_board']
        acft_in_db['water'] = acft['water']
        acft_in_db['dof'] = acft['dof']
        acft_in_db.save()
    return jsonify(msg='ok')


@aircraft.route('/add', methods=['POST'])
def add_aircraft_data():
    aircraft_data = request.get_json()['newAcft']
    tail = aircraft_data['tail'].upper()
    try:
        acft = Aircraft.objects.get(tail=tail)
        acft.water = aircraft_data['water']
        acft.oew = int(aircraft_data['oew']) - 200 - int(aircraft_data['water']) - int(aircraft_data['fak'])
        acft.fak = aircraft_data['fak']
        acft.save()
        return 'ok'

    except DoesNotExist as e:
        acft = Aircraft()
        acft['tail'] = tail
        acft['water'] = aircraft_data['water']
        acft['oew'] = int(aircraft_data['oew']) - 200 - int(aircraft_data['water']) - int(aircraft_data['fak'])
        acft['fak'] = aircraft_data['fak']
        acft.save()
        return 'ok'


