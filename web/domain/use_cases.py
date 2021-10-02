import logging

from web.domain.models.location import Location
from web.domain.models.product import Product
from web.domain.models.relationships import ProductLocations
from web.domain.models.storage import Storage

logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def add_product(data):
    product_id = data.get('product')
    storage_name = data.get('storage')
    location_string = data.get('location')
    quantity = data.get('quantity')

    product = Product.find_by_id(product_id)
    if not product:
        return 'error'
    location = Location.parse(location_string)
    storage = Storage.query.filter_by(name=storage_name).first()

    product_location = ProductLocations.query.filter_by(product=product, location=location, storage=storage).first()
    if product_location:
        product_location.quantity += quantity
    else:
        product_location = ProductLocations(product=product, location=location, storage=storage, quantity=quantity)

    product_location.save()

    return location


