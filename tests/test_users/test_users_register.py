import unittest

from users.users import Users, HTTPStatus
from connections import Connections


class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        company_email = 'company_test_create@test.com'
        email = 'users_test_create@test.com'
        password = '123456789'
        data = {
            "response_name": "Name Test",
            "company_name": "Company Test LTDA",
            "phone": "11951236634",
            "cnpj": "1234567897897845"
        }
        cls.register_provider = Users(email=company_email, password=password, register_data=data, table='provider')
        cls.register_client = Users(email=email, password=password, register_data=data, table='client')

    def test_register_provider(self):
        _, status = self.register_provider.register()
        self.assertEqual(status, HTTPStatus.CREATED)

    def test_register_client(self):
        _, status = self.register_client.register()
        self.assertEqual(status, HTTPStatus.CREATED)

    @classmethod
    def tearDownClass(cls) -> None:
        db = Connections(table_name=None)
        with db.connect() as conn:
            company_email = 'company_test_create@test.com'
            email = 'users_test_create@test.com'
            conn.execute(f"delete from provider where email = '{company_email}'")
            conn.execute(f"delete from client where email = '{email}'")
