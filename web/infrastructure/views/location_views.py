from flask_restplus import Resource
from web.domain.errors import InvalidLocationString, StorageNotFound
from web.domain.use_cases import get_products_in_location
from web.infrastructure import errors
from web.infrastructure.api import api
from web.infrastructure.serializers import error_fields


ns_locations = api.namespace('locations', description='LocationResource')


@ns_locations.route('/<storage>/<location_string>')
class LocationsCollection(Resource):
    @ns_locations.response(200, 'Success')
    @ns_locations.response(400, 'Bad Request', error_fields)
    def get(self, storage, location_string):
        try:
            products = get_products_in_location(storage, location_string)
        except InvalidLocationString:
            raise errors.InvalidLocationString
        except StorageNotFound:
            raise errors.StorageNotFound
        return products, 200