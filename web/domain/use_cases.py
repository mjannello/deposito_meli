import logging

from web.domain.errors import ProductNotFound, LocationIsFull, CanNotAcceptAnotherProduct, ProductIsNotInLocation, \
    CanNotRemoveThatQuantity
from web.domain.models.location import Location
from web.domain.models.product import Product
from web.domain.models.relationships import StoredProducts
from web.domain.models.storage import Storage
from web.domain.utils import validate_location_string
from web.settings import MAX_TYPES_IN_LOCATION
from web.settings import MAX_PRODUCTS_IN_LOCATION

logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def add_product(product_data):
    try:
        input_quantity, location, product, storage = initialize_insertion_deletion_models(product_data)
    except ProductNotFound as e:
        raise e

    types_of_products_stored, quantity_stored = get_type_products_and_quantity_stored(location, storage)

    try:
        can_insert_product(types_of_products_stored, quantity_stored, product.type, input_quantity)
    except (CanNotAcceptAnotherProduct, LocationIsFull) as e:
        raise e

    stored_product_id = StoredProducts.upsert(product=product, location=location, storage=storage, quantity=input_quantity)
    logger.info(f'Stored product id: {stored_product_id}')
    return stored_product_id


def initialize_insertion_deletion_models(product_data):
    product_id = product_data.get('product')
    storage_name = product_data.get('storage')
    location_string = product_data.get('location')
    quantity = product_data.get('quantity')
    product = Product.find_by_id(product_id)
    if not product:
        raise ProductNotFound
    location = Location.parse(location_string)
    storage = Storage.get_storage(storage_name)
    return quantity, location, product, storage


def get_type_products_and_quantity_stored(location, storage):
    stored_products_in_location = StoredProducts.get_all_products_in_location(location=location, storage=storage)
    types_of_products_stored = [sp.product.type for sp in stored_products_in_location]
    quantity_storaged = sum([sp.quantity for sp in stored_products_in_location])
    return types_of_products_stored, quantity_storaged


def can_insert_product(types_of_products_stored, quantity_stored, input_product_type, input_quantity):
    if len(types_of_products_stored) == MAX_TYPES_IN_LOCATION and input_product_type not in types_of_products_stored:
        raise CanNotAcceptAnotherProduct

    if quantity_stored + input_quantity > MAX_PRODUCTS_IN_LOCATION:
        raise LocationIsFull


def remove_product(product_data):
    try:
        removal_quantity, location, product, storage = initialize_insertion_deletion_models(product_data)
    except ProductNotFound as e:
        raise e

    stored_product = StoredProducts.get_product_in_location(product, location, storage)

    try:
        can_remove_product(stored_product, removal_quantity)
    except (ProductIsNotInLocation, CanNotRemoveThatQuantity) as e:
        raise e

    removed_product_id = StoredProducts.remove(stored_product, removal_quantity=removal_quantity)
    logger.info(f'Removed product id: {removed_product_id}')
    return removed_product_id


def can_remove_product(stored_product, removal_quantity):
    if not stored_product:
        raise ProductIsNotInLocation
    if stored_product.quantity < removal_quantity:
        raise CanNotRemoveThatQuantity


def get_products_in_location(storage_name, location_string):
    try:
        validate_location_string(location_string)
    except ValueError as e:
        raise e
    location = Location.parse(location_string)
    storage = Storage.get_storage(storage_name)

    stored_product = StoredProducts.get_all_products_in_location(storage, location)
    products = {sp.product.id: sp.quantity for sp in stored_product if sp.quantity > 0}
    response = {'location': location_string, 'storage':storage_name, 'products': products}
    return response
