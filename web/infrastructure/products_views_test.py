import pytest


@pytest.fixture
def client():
    from web.infrastructure.app import app
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture(scope='function')
def add_product_payload():
    return {
        'product': 1,
        'storage': 'AR01',
        'location': 'AL-02-01-IZ',
        'quantity': 1
    }


class TestAddProduct:
    def test_add_product_successfully(self, mocker, client, add_product_payload):
        mocker.patch('web.domain.use_cases.product_use_cases.add_product',
                     return_value=add_product_payload)
        response = client.post(path='/products/', json=add_product_payload)
        assert response.status_code == 201
        assert response.get_json() == add_product_payload

