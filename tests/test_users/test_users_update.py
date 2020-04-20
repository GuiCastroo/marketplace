import unittest
from users.users import UpdateUsers


class TestAllUpdate(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.update_provider = UpdateUsers(table='provider', email='company_update@test.com', password=None)
        cls.update_client = UpdateUsers(table='client', email='test_update@test.com', password=None)
        cls.email_fake = 'update_email@test.com'
        cls.update_forms = {
            "cnpj": "1234567897897845",
            "phone": "11951236634",
            "company_name": "Company update LTDA",
            "response_name": "Name Test UPDATE"
        }

    def test_update_email_provider(self):
        data, status = self.update_provider.update_email(self.email_fake)
        self.assertEqual(data['data']['email'], self.email_fake)

    def test_update_data_register_provider(self):
        data, status = self.update_provider.update_data_of_register(self.update_forms)
        self.assertEqual(data['data']['registration_form'], self.update_forms)

    def test_update_email_client(self):
        data, status = self.update_client.update_email(self.email_fake)
        self.assertEqual(data['data']['email'], self.email_fake)

    def test_update_data_register_client(self):
        data, status = self.update_client.update_data_of_register(self.update_forms)
        self.assertEqual(data['data']['registration_form'], self.update_forms)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.update_provider.update_email('company_update@test.com')
        cls.update_client.update_email('test_update@test.com')
        cls.update_provider.update_data_of_register(
            {'cnpj': '1234567897897845',
             'phone': '11951236634',
             'company_name': 'Company Test LTDA',
             'response_name': 'Name Test'}
        )
        cls.update_client.update_data_of_register(
            {"cnpj": "1234567897897845",
             "phone": "11951236634",
             "company_name": "Company Test LTDA",
             "response_name": "Name Test"}
        )
