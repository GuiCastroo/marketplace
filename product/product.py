from connections import Connections
import boto3
import uuid
from http import HTTPStatus


class RegisterProduct(Connections):
    def __init__(self, provide_id, price, description, data_product):
        super().__init__(table_name='tb_product')
        self.provide_id = provide_id
        self.price = price
        self.description = description
        self.data_product = data_product

    def register_product(self):
        with self.connect() as conn:
            conn.execute(
                self.table.insert(),
                product_id=str(uuid.uuid4()),
                price=self.price,
                description=self.description,
                data_product=self.data_product
            )

    def upload_photo_s3(self):
        object = self.data_product


class RegisterStock(Connections):
    ...


