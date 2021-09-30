import marshmallow
from flask import request
from flask_restplus import Resource
from marshmallow import Schema, fields

from web import schemas
from web.api import api
from web.views.serializers import add_product_fields, error_fields

ns_products = api.namespace('products', description='Product Resource')


@ns_products.route('/')
class ProductsCollection(Resource):
    add_product_schema = schemas.AddProduct()
    @ns_products.response(201, 'Success')
    @ns_products.response(400, 'Bad Request', error_fields)
    @api.expect(add_product_fields, validate=True)
    def post(self):
        try:
            product_data = self.add_product_schema.load(request.json)
        except marshmallow.ValidationError as e:
            raise ValueError(e)
        return 'first endpoint working', 200
