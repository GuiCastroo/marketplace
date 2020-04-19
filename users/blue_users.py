from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from users.serealizer import LoginSchema, ProvideRegisterSchema, ClientRegisterSchema, ConfirmationUserSchema, \
    UpdateEmailSchema, UpdateFormsSchema, ChangePasswordSchema
from users.users import Users, ConfirmationUser, UpdateUsers, HTTPStatus

blue_users = Blueprint('users', __name__)


@blue_users.route('/login/<type_user>', methods=['GET', 'POST'])
def login(type_user):
    data = request.get_json()
    try:
        schema = LoginSchema()
        schema.load(data=data)
    except ValidationError as error:
        return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    user = Users(email=data['email'], password=data['password'], table=type_user)
    message, status = user.login()
    return jsonify({'message': message}), status


@blue_users.route('/register/<type_user>', methods=['POST'])
def register(type_user):
    data = request.get_json()
    try:
        if type_user == 'provider':
            schema = ProvideRegisterSchema()
            schema.load(data=data)
        else:
            schema = ClientRegisterSchema()
            schema.load(data=data)
    except ValidationError as error:
        return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    user = Users(email=data['email'], password=data['password'], table=type_user, register_data=data['forms'])
    message, status = user.register()
    return jsonify({"message": message}), status


@blue_users.route('/confirmation/<type_user>', methods=['PUT'])
def confirmation_user(type_user):
    data = request.get_json()
    try:
        schema = ConfirmationUserSchema()
        schema.load(data=data)
    except ValidationError as error:
        return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    confirmation = ConfirmationUser(type_user, data['user_id'])
    message, status = confirmation.confirmation()
    return jsonify({'message': message}), status


@blue_users.route('/change_password/<type_user>', methods=['PUT'])
def change_password(type_user):
    data = request.get_json()
    try:
        schema =  ChangePasswordSchema()
        schema.load(data)
    except ValidationError as error:
        return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    update_user = UpdateUsers(table=type_user, email=data['email'], password=None)
    message, status = update_user.change_password(data['new_password'])
    return jsonify({'message': message}), status


@blue_users.route('/update/<type_user>/<update_>', methods=['PUT'])
def update_user_(type_user, update_):
    data = request.get_json()
    update_user = UpdateUsers(table=type_user, email=data['email'], password=None)
    if update_ == 'register':
        try:
            schema = UpdateEmailSchema()
            schema.load(data)
            message, status = update_user.update_data_of_register(data['forms'])
            return jsonify(message), status
        except ValidationError as error:
            return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    elif update_ == 'email':
        try:
            schema = UpdateFormsSchema()
            schema.load(data)
            message, status = update_user.update_email(data['email'])
            return jsonify(message), status
        except ValidationError as error:
            return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    else:
        return jsonify({'message': f"Not found {update_} method to update"}), HTTPStatus.NOT_FOUND
