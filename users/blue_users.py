from flask import Blueprint, jsonify, request
import json

from users.users import Users

blue_users = Blueprint('users', __name__)


@blue_users.route('/login/<type_user>', methods=['GET', 'POST'])
def login(type_user):
    data = request.get_json()
    user = Users(email=data['email'], password=data['password'], table=type_user)
    message, status = user.login()
    return jsonify({'message': message}), status


@blue_users.route('/register/<type_user>', methods=['POST'])
def register(type_user):
    data = request.get_json()
    user = Users(email=data['email'], password=data['password'], table=type_user, register_data=data['forms'])
    message, status = user.register()
    return jsonify(message), status
