import unittest
from users.users import Users, HTTPStatus


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Data exist in database
        email_company = 'company_test@test.com'
        email_client = 'users_test@test.com'
        password = '84624375'
        cls.class_users_provider_ok = Users(email=email_company, password=password, table='provider')
        cls.class_users_client_ok = Users(email=email_client, password=password, table='client')

        # Password to be incorrect
        password_incorrect = '1234'
        cls.class_users_provider_password_incorrect = Users(
            email=email_company, password=password_incorrect, table='provider'
        )
        cls.class_users_client_password_incorrect = Users(
            email=email_client, password=password_incorrect, table='client'
        )

        # Data is not exist in database
        email_false = 'users_false_test@test.com'
        password_false = '123456789'
        cls.class_users_provider_is_not_ok = Users(email=email_false, password=password_false, table='provider')
        cls.class_users_client_is_not_ok = Users(email=email_false, password=password_false, table='client')

    def test_login_provider_with_data_is_ok(self):
        _, status = self.class_users_provider_ok.login()
        self.assertEqual(status, HTTPStatus.OK)

    def test_login_client_with_data_is_ok(self):
        _, status = self.class_users_client_ok.login()
        self.assertEqual(status, HTTPStatus.OK)

    def test_login_provider_with_password_incorrect(self):
        _, status = self.class_users_provider_password_incorrect.login()
        self.assertEqual(status, HTTPStatus.BAD_REQUEST)

    def test_login_client_with_password_incorrect(self):
        _, status = self.class_users_client_password_incorrect.login()
        self.assertEqual(status, HTTPStatus.BAD_REQUEST)

    def test_login_provider_with_data_is_not_ok(self):
        _, status = self.class_users_provider_is_not_ok.login()
        self.assertEqual(status, HTTPStatus.NOT_FOUND)

    def test_login_client_with_data_is_not_ok(self):
        _, status = self.class_users_client_is_not_ok.login()
        self.assertEqual(status, HTTPStatus.NOT_FOUND)


if __name__ == '__main__':
    unittest.main()
