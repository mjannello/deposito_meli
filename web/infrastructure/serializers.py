from flask_restplus import fields

from web.infrastructure.api import api

add_product_fields = api.model(
    'Add product fields',
    {
        'product': fields.String(example="MLB12345"),
        'storage': fields.String(example="AR01"),
        'location': fields.String(example="LM-00-00-IZ"),
        'quantity': fields.Integer(example=10)
    }
)

remove_product_fields = api.model(
    'Remove product fields',
    {
        'product': fields.String(example="MLB12345"),
        'storage': fields.String(example="AR01"),
        'location': fields.String(example="LM-00-00-IZ"),
        'quantity': fields.Integer(example=10)
    }
)

error_fields = api.model(
    'Error',
    {
        'title': fields.String(example="Not Found"),
        'message': fields.String(example="The requested resource was not found"),
        'status_code': fields.String(example="404"),
        'error_code': fields.Integer(example='NOT-FOUND')
    }
)
