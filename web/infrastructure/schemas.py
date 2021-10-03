from marshmallow import Schema, fields, validates

import re


class Error(Schema):
    title = fields.String(required=True)
    message = fields.String(required=True)
    status_code = fields.String(required=True)
    error_code = fields.String(required=True)

    
class AddProduct(Schema):
    product = fields.Integer(required=True)
    storage = fields.String(required=True)
    location = fields.String(required=True)
    quantity = fields.Integer(required=True)

    @validates('location')
    def validate_location(self, value):
        r = re.compile("^[A-Z]{2}-\d{2}-\d{2}-(DE|IZ)$")
        if not r.match(value):
            raise ValueError


class RemoveProduct(Schema):
    product = fields.Integer(required=True)
    storage = fields.String(required=True)
    location = fields.String(required=True)
    quantity = fields.Integer(required=True)

    @validates('location')
    def validate_location(self, value):
        r = re.compile("^[A-Z]{2}-\d{2}-\d{2}-(DE|IZ)$")
        if not r.match(value):
            raise ValueError


class ReadLocation(Schema):
    storage = fields.String(required=True)
    location = fields.String(required=True)
    products = fields.Dict(required=True)


class SearchLocation(Schema):
    product = fields.String(required=True)
    storage = fields.String(required=True)
    locations = fields.List(fields.Dict(), required=True)

