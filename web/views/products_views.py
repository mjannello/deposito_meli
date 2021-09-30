from flask_restplus import Resource
from marshmallow import Schema, fields

from web.api import api
from web.views.serializers import add_product_fields, error_fields

ns_products = api.namespace('products', description='Product Resource')


@ns_products.route('/')
class ProductsCollection(Resource):
    @ns_products.response(201, 'Success')
    @ns_products.response(400, 'Bad Request', error_fields)
    @api.expect(add_product_fields, validate=True)
    def post(self):
        return 'first endpoint working', 200
