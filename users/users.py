import uuid
from http import HTTPStatus

from werkzeug.security import generate_password_hash, check_password_hash

from connections import Connections


class Users(Connections):
    def __init__(self, email, password, table, register_data=None):
        super().__init__(table_name=table)
        self.email = email
        self.password = password
        self.register_data = register_data
        self.data_user = self.get_user()

    def get_user(self):
        return self.table.select(self.table.c.email == self.email).execute().first()

    def register(self):
        if self.data_user:
            return f'The Customer already exist in the database: {self.email}', HTTPStatus.CONFLICT
        else:
            hash_password = generate_password_hash(self.password)
            with self.connect() as conn:
                conn.execute(
                    self.table.insert(),
                    id=str(uuid.uuid4()),
                    email=self.email,
                    password=hash_password,
                    registration_form=self.register_data
                )
            return "successful registration", HTTPStatus.CREATED

    def login(self):
        if self.data_user:
            check_password = check_password_hash(self.data_user.password, self.password)
            return ({'text': 'data is correct', '_id': self.data_user.id}, HTTPStatus.OK) if check_password \
                else ('data is not correct', HTTPStatus.BAD_REQUEST)
        else:
            return F'{self.email}  is not found', HTTPStatus.NOT_FOUND


class UpdateUsers(Users):
    def change_password(self, new_password):
        new_password = generate_password_hash(new_password)
        with self.connect() as conn:
            conn.excute(
                self.table.update().where(self.table.c.id == self.data_user.id).values(password=new_password)
            )
        return "Change with success", HTTPStatus.NO_CONTENT

    def update_data_of_register(self, new_data):
        with self.connect() as conn:
            conn.execute(
                self.table.update().where(self.table.c.id == self.data_user.id).values(registration_form=new_data)
            )
        data = self.get_user()
        return {'message': "Change with success", 'data': data}, HTTPStatus.NO_CONTENT

    def update_email(self, new_email):
        with self.connect() as conn:
            conn.execute(
                self.table.update().where(self.table.c.id == self.data_user.id).values(email=new_email)
            )
        self.email = new_email
        data = self.get_user()
        return {'message': "Change with success", 'data': data}, HTTPStatus.NO_CONTENT


class ConfirmationUser(Connections):
    def __init__(self, table, user_id):
        super().__init__(table_name=table)
        self.id = user_id

    def confirmation(self):
        with self.connect() as conn:
            conn.execute(
                self.table.update().where(self.table.c.id == self.id).values(active=True)
            )
        return 'Confirmation with success', HTTPStatus.NO_CONTENT



