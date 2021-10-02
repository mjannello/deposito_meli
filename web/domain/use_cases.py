import logging

from web.domain.errors import ProductDoesNotExist, LocationIsFull, CanNotAcceptAnotherProduct
from web.domain.models.location import Location
from web.domain.models.product import Product
from web.domain.models.relationships import StoredProducts
from web.domain.models.storage import Storage
from web.settings import MAX_TYPES_IN_LOCATION
from web.settings import MAX_PRODUCTS_IN_LOCATION

logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def add_product(data):
    product_id = data.get('product')
    storage_name = data.get('storage')
    location_string = data.get('location')
    input_quantity = data.get('quantity')

    product = Product.find_by_id(product_id)
    if not product:
        raise ProductDoesNotExist

    location = Location.parse(location_string)
    storage = Storage.get_storage(storage_name)

    types_of_products, quantity_stored = get_products_in_location(location, storage)

    try:
        can_insert_product(types_of_products, quantity_stored, product.type, input_quantity)
    except (CanNotAcceptAnotherProduct, LocationIsFull) as e:
        raise e

    stored_product_id = StoredProducts.upsert(product=product, location=location, storage=storage, quantity=input_quantity)
    logger.info(f'Stored product id: {stored_product_id}')
    return stored_product_id


def get_products_in_location(location, storage):
    stored_products_in_location = StoredProducts.query.filter_by(location=location, storage=storage).all()
    types_of_products = [sp.product.type for sp in stored_products_in_location]
    quantity_storaged = sum([sp.quantity for sp in stored_products_in_location])
    return types_of_products, quantity_storaged


def can_insert_product(types_of_products_stored, quantity_stored, input_product_type, input_quantity):
    if len(types_of_products_stored) == MAX_TYPES_IN_LOCATION and input_product_type not in types_of_products_stored:
        raise CanNotAcceptAnotherProduct

    if quantity_stored + input_quantity > MAX_PRODUCTS_IN_LOCATION:
        raise LocationIsFull
