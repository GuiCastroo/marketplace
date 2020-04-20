from marshmallow import fields, Schema
from marshmallow.validate import Length


class LoginSchema(Schema):
    class Meta:
        ordered = True
    email = fields.String(required=True)
    password = fields.String(required=True)


class ProvideFormsSchema(Schema):
    company_name = fields.String(required=True)
    response_name = fields.String(required=True)
    phone = fields.String(required=True)
    cnpj = fields.String(required=True, validate=[Length(equal=16, error="CNPJ must have of 16 characters")])


class ProvideRegisterSchema(Schema):
    class Meta:
        ordered = True
    email = fields.Email(required=True)
    password = fields.String(required=True)
    forms = fields.Nested(ProvideFormsSchema, required=True)


class ClientFormsSchema(Schema):
    company_name = fields.String(required=True)
    response_name = fields.String(required=True)
    phone = fields.String(required=True)
    cnpj = fields.String(required=True, validate=[Length(equal=16, error="CNPJ must have of 16 characters")])


class ClientRegisterSchema(Schema):
    class Meta:
        ordered = True
    email = fields.Email(required=True)
    password = fields.String(required=True)
    forms = fields.Nested(ClientFormsSchema, required=True)


class ConfirmationUserSchema(Schema):
    class Meta:
        ordered = True
    user_id = fields.String


class UpdateEmailSchema(Schema):
    class Meta:
        ordered = True
    email = fields.Email(required=True)
    new_email = fields.Email(required=True)


class UpdateFormsSchema(Schema):
    class Meta:
        ordered = True
    email = fields.Email(required=True)
    forms = fields.Nested(ProvideFormsSchema, required=True)


class ChangePasswordSchema(Schema):
    class Meta:
        ordered = True
    email = fields.Email(required=True)
    new_password = fields.String(required=True)