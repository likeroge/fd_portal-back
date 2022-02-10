import requests as requests
from flask import Blueprint, jsonify

users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/all', methods=['GET'])
def all_users():
    return jsonify({'msg': "Hello World"})


@users.route('/test')
def test_users():
    data = requests.get('https://jsonplaceholder.typicode.com/users')
    return jsonify(data.json())
