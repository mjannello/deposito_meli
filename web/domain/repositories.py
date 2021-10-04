import requests
import logging

from web.infrastructure import errors

logger = logging.getLogger(__name__)

MELI_REPOSITORY_API_URL = 'https://api.mercadolibre.com/items/'


class MeliRepository:
    def __init__(self):
        self.api_url = MELI_REPOSITORY_API_URL

    def check_logistic_type(self, product_id):
        response = requests.get(
            self.api_url.format(product_id)
        )

        if response.status_code == 404:
            logger.error('Error Product was not found')
            raise errors.ProductIsNotInLocationError
        if response.status_code == 200:
            return response.json()['logistic_type'] == 'fulfillment'