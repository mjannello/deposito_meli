import logging

from sqlalchemy.exc import SQLAlchemyError

from web.domain.errors import StorageNotFound, ProductNotFound, InvalidProductId
from web.domain.models.product import Product
from web.domain.models.relationships import StoredProducts
from web.domain.models.storage import Storage

logger = logging.getLogger(__name__)


def search_locations_in_storage(storage_name, product_id):
    """Method to search all locations from the given storage that contains given product_id"""
    storage = Storage.get_storage(storage_name)
    if not storage:
        raise StorageNotFound
    try:
        product = Product.find_by_id(product_id)
    except InvalidProductId as e:
        raise e
    if not product:
        raise ProductNotFound
    try:
        stored_products = StoredProducts.get_locations_in_storage(storage, product)
    except SQLAlchemyError:
        raise
    locations = []
    for sp in stored_products:
        locations.append({
            'area': sp.location.area,
            'hall': sp.location.hall,
            'row': sp.location.row,
            'side': sp.location.side,
            'quantity': sp.quantity})

    return {'product': product_id, 'storage': storage_name, 'locations': locations}