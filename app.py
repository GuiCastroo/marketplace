from flask import Flask, jsonify, request
from http import HTTPStatus
from users.blue_users import blue_users

app = Flask('__name__')
app.register_blueprint(blue_users)


@app.route('/')
def home():
    return jsonify({'Message': 'Welcome the API  marketplace'}), HTTPStatus.OK


if __name__ == '__main__':
    app.run()


