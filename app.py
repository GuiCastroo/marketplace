from flask import Flask, jsonify, request
from http import HTTPStatus
from users.blue_users import blue_users
from emails import SendEmailHTML
app = Flask('__name__')
app.register_blueprint(blue_users)


@app.route('/')
def home():
    return jsonify({'Message': 'Welcome the API  marketplace'}), HTTPStatus.OK


@app.route('/send-email/html', methods=['POST'])
def send_email():
    data = request.get_json()
    email = SendEmailHTML(from_email=data['from_email'], html=data['html'], subject=data['subject'])
    return email.send_email()


if __name__ == '__main__':
    app.run()


