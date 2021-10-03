import requests
import logging

from web.infrastructure import errors

logger = logging.getLogger(__name__)


class MeliRepository:
    def __init__(self, api_url):
        self.api_url = api_url

    def check_logistic_type(self, product_id):
        response = requests.get(
            self.api_url.format(product_id)
        )

        if response.status_code == 404:
            logger.error('Error Product was not found')
            raise errors.ProductIsNotInLocation
        if response.status_code == 200:
            return response.json()['logistic_type'] == 'fulfillment'