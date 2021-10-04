import logging
import marshmallow

from flask import request
from flask_restplus import Resource

from web.infrastructure import schemas, errors
from web.infrastructure.api import api
from web.domain.errors import ProductNotFound, CanNotAcceptAnotherProduct, LocationIsFull, ProductIsNotInLocation, \
    CanNotRemoveThatQuantity
from web.domain.use_cases.product_use_cases import add_product, remove_product
from web.infrastructure.serializers import add_product_fields, error_fields, remove_product_fields

logger = logging.getLogger(__name__)

ns_products = api.namespace('products', description='Product Resource')
error_schema = schemas.Error()


@api.errorhandler(errors.Error)
def error_handler(error):
    return error_schema.dump(error), error.status_code


@ns_products.route('/')
class ProductsCollection(Resource):
    add_product_schema = schemas.AddProduct()
    remove_product_schema = schemas.RemoveProduct()

    @ns_products.response(201, 'Inserted', add_product_fields)
    @ns_products.response(400, 'Bad Request', error_fields)
    @ns_products.response(404, 'Not Found', error_fields)
    @api.expect(add_product_fields, validate=True)
    def post(self):
        try:
            product_data = self.add_product_schema.load(request.json)
        except marshmallow.ValidationError as e:
            return ValueError(e)
        try:
            stored_product = add_product(product_data)
        except ProductNotFound:
            raise errors.ProductNotFound
        except CanNotAcceptAnotherProduct:
            raise errors.CanNotAcceptAnotherProduct
        except LocationIsFull:
            raise errors.LocationFull
        logger.info(f'product_data: {product_data}')

        return self.add_product_schema.dump(stored_product), 201

    @ns_products.response(202, 'Removed', remove_product_fields)
    @ns_products.response(400, 'Bad Request', error_fields)
    @api.expect(remove_product_fields, validate=True)
    def put(self):
        try:
            product_data = self.remove_product_schema.load(request.json)
        except marshmallow.ValidationError as e:
            raise ValueError(e)
        try:
            removed_product = remove_product(product_data)
        except ProductNotFound:
            raise errors.ProductNotFound
        except ProductIsNotInLocation:
            raise errors.ProductIsNotInLocation
        except CanNotRemoveThatQuantity:
            raise errors.CanNotRemoveThatQuantity

        return self.remove_product_schema.dump(removed_product), 202


