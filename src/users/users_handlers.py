import requests as requests
from flask import Blueprint, jsonify
from mongoengine import Document

users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/all', methods=['GET'])
def all_users():
    return jsonify({'msg': "Hello World"})


@users.route('/test')
def test_users():
    # posts = Posts.objects()
    # for post in posts:
    #     print(post.date)
    # print(posts)
    data = requests.get('https://jsonplaceholder.typicode.com/users')
    return jsonify(data.json())

