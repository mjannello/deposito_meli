class Error(Exception):
    @property
    def title(self):
        raise NotImplementedError

    @property
    def message(self):
        raise NotImplementedError

    @property
    def status_code(self):
        raise NotImplementedError

    @property
    def error_code(self):
        raise NotImplementedError


class ProductNotFound(Error):
    title = 'Product not found'
    message = 'The requested product was not found'
    status_code = 404
    error_code = 'PRODUCT-NOT-FOUND'


class CanNotAcceptAnotherProduct(Error):
    title = 'Can not accept another product'
    message = 'Maximum of different type of products was reached in this location'
    status_code = 404
    error_code = 'PRODUCT-NOT-ACCEPTED'


class LocationFull(Error):
    title = 'Location full'
    message = 'Can not insert this much of products in this location'
    status_code = 400
    error_code = 'LOCATION-FULL'


class ProductIsNotInLocation(Error):
    title = 'Product Is Not In current Location'
    message = 'The product you are trying to remove is not in this location'
    status_code = 400
    error_code = 'PRODUCT-NOT-IN-LOCATION'


class CanNotRemoveThatQuantity(Error):
    title = 'Cannot remove that quantity'
    message = 'There is no that much products in this location'
    status_code = 400
    error_code = 'PRODUCT-INVALID-QUANTITY'


class StorageNotFound(Error):
    title = 'Storage not found'
    message = 'Storage could not be found'
    status_code = 404
    error_code = 'STORAGE-NOT-FOUND'


class InvalidLocationString(Error):
    title = 'Invalid Location String'
    message = 'Location string is malformed'
    status_code = 400
    error_code = 'LOCATION-MALFORMED'
