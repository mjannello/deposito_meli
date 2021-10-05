import pytest

from web.domain.errors import ProductNotFound, CanNotAcceptAnotherProduct, LocationIsFull
from web.domain.use_cases.product_use_cases import add_product, initialize_insertion_deletion_models, can_insert_product,\
    remove_product


@pytest.fixture
def mocked_product_insert_data():
    return {
        "product": 1,
        "storage": "AR01",
        "location": "AL-02-00-IZ",
        "quantity": 1
    }


@pytest.fixture
def mocked_product_remove_data():
    return {
        "product": 1,
        "storage": "AR01",
        "location": "AL-02-00-IZ",
        "quantity": 1
    }


class TestAddProduct:

    def test_add_product_product_not_found(self, mocker):
        mocker.patch('web.domain.use_cases.product_use_cases.initialize_insertion_deletion_models',
                     side_effect=ProductNotFound)
        with pytest.raises(ProductNotFound):
            add_product(mocked_product_insert_data)

    def test_add_product_cannot_insert_max_type_of_products_reached(self, mocker):
        class MockProduct:
            type = 'fake_type'
        mocker.patch('web.domain.use_cases.product_use_cases.initialize_insertion_deletion_models',
                     return_value=[1, 'some_stg', MockProduct, 10])
        mocker.patch('web.domain.use_cases.product_use_cases.get_type_products_and_quantity_stored', return_value=['fake_type', 1])
        mocker.patch('web.domain.use_cases.product_use_cases.can_insert_product', side_effect=CanNotAcceptAnotherProduct)
        with pytest.raises(CanNotAcceptAnotherProduct):
            add_product(mocked_product_insert_data)

    def test_add_product_cannot_insert_location_is_full(self, mocker):
        class MockProduct:
            type = 'fake_type'
        mocker.patch('web.domain.use_cases.product_use_cases.initialize_insertion_deletion_models',
                     return_value=[1, 'some_stg', MockProduct, 10])
        mocker.patch('web.domain.use_cases.product_use_cases.get_type_products_and_quantity_stored', return_value=['fake_type', 1])
        mocker.patch('web.domain.use_cases.product_use_cases.can_insert_product', side_effect=LocationIsFull)
        with pytest.raises(LocationIsFull):
            add_product(mocked_product_insert_data)

    def test_initialize_insertion_deletion_models_successfully(self, mocker, mocked_product_insert_data):
        mocker.patch('web.domain.models.product.Product.find_by_id', return_value='product')
        mocker.patch('web.domain.models.location.Location.parse', return_value='location')
        mocker.patch('web.domain.models.storage.Storage.get_storage', return_value='stg')
        assert initialize_insertion_deletion_models(mocked_product_insert_data) == (1, 'location', 'product', 'stg')

    def test_initialize_insertion_deletion_models_product_is_none(self, mocker, mocked_product_insert_data):
        mocker.patch('web.domain.models.product.Product.find_by_id', return_value=None)
        mocker.patch('web.domain.models.location.Location.parse', return_value='location')
        mocker.patch('web.domain.models.storage.Storage.get_storage', return_value='stg')
        with pytest.raises(ProductNotFound):
            initialize_insertion_deletion_models(mocked_product_insert_data)

    def test_can_insert_product_cannot_accept_another_product(self):
        with pytest.raises(CanNotAcceptAnotherProduct):
            can_insert_product(['type1', 'type2', 'type3'], 10, 'type 4', 30)

    def test_can_insert_product_location_is_full(self):
        with pytest.raises(LocationIsFull):
            can_insert_product(['type1'], 90, 'type 2', 20)


class TestRemoveProduct:
    def test_remove_product(self, mocker):
        mocker.patch('web.domain.use_cases.product_use_cases.initialize_insertion_deletion_models', side_effect=ProductNotFound)
        with pytest.raises(ProductNotFound):
            remove_product(mocked_product_remove_data)
