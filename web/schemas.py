from marshmallow import Schema, fields, validates, validate

import re
# r = re.compile("^[A-Z]{2}-\d{2}-\d{2}-(DE|IZ)$")
# if r.match('x/x/xxxx xx:xx') is not None:
#    print 'matches'


class AddProduct(Schema):
    product = fields.String(required=True)
    storage = fields.String(required=True)
    location = fields.String(required=True)
    quantity = fields.Integer(required=True)

    @validates('location')
    def validate_location(self, value):
        r = re.compile("^[A-Z]{2}-\d{2}-\d{2}-(DE|IZ)$")
        if not r.match(value):
            raise ValueError
