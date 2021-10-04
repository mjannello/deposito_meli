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


class ProductNotFoundError(Error):
    title = 'Product not found'
    message = 'The requested product was not found'
    status_code = 404
    error_code = 'PRODUCT-NOT-FOUND'


class CanNotAcceptAnotherProductError(Error):
    title = 'Can not accept another product'
    message = 'Maximum of different type of products was reached in this location'
    status_code = 404
    error_code = 'PRODUCT-NOT-ACCEPTED'


class InvalidProductIdError(Error):
    title = 'Given product id is not valid'
    message = 'The given product id is not a valid a id'
    status_code = 400
    error_code = 'PRODUCT-NOT-VALID'


class LocationFullError(Error):
    title = 'Location full'
    message = 'Can not insert this much of products in this location'
    status_code = 400
    error_code = 'LOCATION-FULL'


class ProductIsNotInLocationError(Error):
    title = 'Product Is Not In current Location'
    message = 'The product you are trying to remove is not in this location'
    status_code = 400
    error_code = 'PRODUCT-NOT-IN-LOCATION'


class CanNotRemoveThatQuantityError(Error):
    title = 'Cannot remove that quantity'
    message = 'There is no that much products in this location'
    status_code = 400
    error_code = 'PRODUCT-INVALID-QUANTITY'


class StorageNotFoundError(Error):
    title = 'Storage not found'
    message = 'Storage could not be found'
    status_code = 404
    error_code = 'STORAGE-NOT-FOUND'


class InvalidLocationStringError(Error):
    title = 'Invalid Location String'
    message = 'Location string is malformed'
    status_code = 400
    error_code = 'LOCATION-MALFORMED'


class InsertingDataError(Error):
    title = 'Something went wrong inserting'
    message = 'Something went wrong trying to insert the current product'
    status_code = 500
    error_code = 'INSERTING-ERROR'
