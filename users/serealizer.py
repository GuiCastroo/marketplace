from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow.validate import Range

MA = Marshmallow()


def configure(app):
    MA.init_app(app)


class ProvideSchema(MA.ModelSchema):
    class Meta:
        ordered = True
    cnpj = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    responsible_name = fields.String(requeried=True)
    responsible_cel = fields.String(required=True)
    site = fields.URL()
    state_registration = fields.String(required=True)
    responsible_phone = fields.String(required=True)
    responsible_position = fields.String(required=True)
    company_name = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip_code = fields.String(required=True)


class CLintSchema(MA.ModelSchema):
    class Meta:
        ordered = True
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    first_name = fields.String(requeried=True)
    last_name = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip_code = fields.String(required=True)
    date_birth = fields.Date(required=True)
    cell = fields.String()
    phone = fields.String()
    number_house = fields.Number(required=True)
    complement = fields.String()
