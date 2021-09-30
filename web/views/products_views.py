from flask_restplus import Resource

from web.api import api

ns_products = api.namespace('products', description='Product Resource')


@ns_products.route('/')
class ProductsCollection(Resource):
    def get(self):
        return 'first endpoint working', 200