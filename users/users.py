import uuid

from werkzeug.security import generate_password_hash, check_password_hash

from connections import Connections
from http import HTTPStatus


class Users(Connections):
    def __init__(self, email, password, table, register_data=None):
        super().__init__(table_name=table)
        self.email = email
        self.password = password
        self.register_data = register_data

    def _get_user(self):
        return self.table.select(self.table.c.email == self.email).execute().first()

    def register(self):
        if self._get_user():
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
        get_user = self._get_user()
        if get_user:
            check_password = check_password_hash(get_user['password'], self.password)
            return ('data is correct', HTTPStatus.OK) if check_password else ('data is not correct',
                                                                              HTTPStatus.BAD_REQUEST)
        else:
            return F'{self.email}  is not found', HTTPStatus.NOT_FOUND

    @property
    def forgot_password(self):
        return self.password

    @forgot_password.setter
    def forgot_password(self, new_password):
        password_modification = generate_password_hash(new_password)
        with self.connect() as conn:
            conn.execute(
                self.table.update().where(self.table.c.email == self.email).values(password=password_modification)
            )
        self.password = new_password


class Provider(Users):

    def edit_register_data(self, new_data):
        ...

    def deleted(self):
        ...


class Client(Users):

    def edit_register_data(self, new_data):
        ...

    def deleted(self):
        ...
