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


