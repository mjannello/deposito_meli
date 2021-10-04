import logging

from web.domain.errors import StorageNotFound, ProductNotFound
from web.domain.models.product import Product
from web.domain.models.relationships import StoredProducts
from web.domain.models.storage import Storage

logger = logging.getLogger(__name__)


def search_locations_in_storage(storage_name, product_id):
    storage = Storage.get_storage(storage_name)
    if not storage:
        raise StorageNotFound
    product = Product.find_by_id(product_id)
    if not product:
        raise ProductNotFound

    stored_products = StoredProducts.get_locations_in_storage(storage, product)
    locations = []
    for sp in stored_products:
        locations.append({
            'area': sp.location.area,
            'hall': sp.location.hall,
            'row': sp.location.row,
            'side': sp.location.side,
            'quantity': sp.quantity})

    return {'product': product_id, 'storage': storage_name, 'locations': locations}