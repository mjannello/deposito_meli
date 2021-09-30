from marshmallow import Schema, fields


class AddProduct(Schema):
    product = fields.String(required=True)
    storage = fields.String(required=True)
    location = fields.String(required=True)
    quantity = fields.Integer(required=True)
