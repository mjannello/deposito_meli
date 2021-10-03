from flask_restplus import Resource

from web.domain.errors import ProductNotFound, ProductIsNotInLocation, CanNotRemoveThatQuantity
from web.domain.use_cases import search_locations_in_storage
from web.infrastructure import errors
from web.infrastructure.api import api
from web.infrastructure.serializers import error_fields

ns_search = api.namespace('search', description='SearchResource')


@ns_search.route('/<storage>/<product_id>')
class SearchCollection(Resource):
    @ns_search.response(200, 'Success')
    @ns_search.response(400, 'Bad Request', error_fields)
    def get(self, storage, product_id):
        try:
            products = search_locations_in_storage(storage, product_id)
        except ProductNotFound:
            raise errors.ProductNotFound
        except (ProductIsNotInLocation, CanNotRemoveThatQuantity) as e:
            return 'error', 400

        return products, 200