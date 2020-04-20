import unittest
from users.users import ConfirmationUser, HTTPStatus
from connections import Connections


class ConfirmationEmail(unittest.TestCase):

    def setUp(self) -> None:
        self._id = '538a10fe-1673-44f2-a929-646a20986e54'
        self.confirmation = ConfirmationUser('provider', self._id)

    def test_confirmation_email(self):
        _, status = self.confirmation.confirmation()
        self.assertEqual(status, HTTPStatus.NO_CONTENT)

    def tearDown(self) -> None:
        db = Connections(table_name='provider')
        with db.connect() as conn:
            conn.execute(
                 db.table.update().where(db.table.c.id == self._id).values(active=None)
            )
