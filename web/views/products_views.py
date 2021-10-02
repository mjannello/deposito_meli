import logging
import marshmallow

from flask import request
from flask_restplus import Resource

from web import schemas
from web.api import api
from web.domain.errors import ProductNotFound, CanNotAcceptAnotherProduct, LocationIsFull, ProductIsNotInLocation, \
    CanNotRemoveThatQuantity
from web.domain.use_cases import add_product, remove_product
from web.serializers import add_product_fields, error_fields, remove_product_fields

logger = logging.getLogger(__name__)

ns_products = api.namespace('products', description='Product Resource')


@ns_products.route('/')
class ProductsCollection(Resource):
    add_product_schema = schemas.AddProduct()
    remove_product_schema = schemas.RemoveProduct()

    @ns_products.response(201, 'Success')
    @ns_products.response(400, 'Bad Request', error_fields)
    @api.expect(add_product_fields, validate=True)
    def post(self):
        try:
            product_data = self.add_product_schema.load(request.json)
        except marshmallow.ValidationError as e:
            return ValueError(e)
        try:
            stored_product_id = add_product(product_data)
        except (ProductNotFound, CanNotAcceptAnotherProduct, LocationIsFull) as e:
            return 'error', 400
        logger.info(f'product_data: {product_data}')

        return stored_product_id, 200

    @ns_products.response(202, 'Success')
    @ns_products.response(400, 'Bad Request', error_fields)
    @api.expect(remove_product_fields, validate=True)
    def put(self):
        try:
            product_data = self.remove_product_schema.load(request.json)
        except marshmallow.ValidationError as e:
            return ValueError(e)
        try:
            removed_product_id = remove_product(product_data)
        except (ProductNotFound, ProductIsNotInLocation, CanNotRemoveThatQuantity) as e:
            return 'error', 400
        logger.info(f'product_data: {product_data}')

        return removed_product_id, 200
