from flask_restplus import Resource
from sqlalchemy.exc import SQLAlchemyError

from web.domain.errors import ProductNotFound, StorageNotFound, InvalidProductId
from web.domain.use_cases.locations_use_cases import search_locations_in_storage
from web.infrastructure import errors, schemas
from web.infrastructure.api import api
from web.infrastructure.serializers import error_fields

ns_search = api.namespace('search', description='SearchResource')


@ns_search.route('/<storage>/<product_id>')
class SearchCollection(Resource):
    search_location_schema = schemas.SearchLocation()

    @ns_search.response(200, 'Success')
    @ns_search.response(400, 'Bad Request', error_fields)
    def get(self, storage, product_id):
        try:
            locations = search_locations_in_storage(storage, product_id)
        except InvalidProductId:
            raise errors.InvalidProductIdError
        except ProductNotFound:
            raise errors.ProductNotFoundError
        except StorageNotFound:
            raise errors.StorageNotFoundError
        except SQLAlchemyError:
            raise errors.FetchingDataError
        return self.search_location_schema.dump(locations), 200
