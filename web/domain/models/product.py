import logging

from sqlalchemy.exc import DataError

from web.domain.errors import InvalidProductId
from web.domain.models.db import db


logger = logging.getLogger(__name__)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    stored_products = db.relationship('StoredProducts', back_populates='product')

    @classmethod
    def find_by_id(cls, _id):
        logger.debug(f'Find product by id: {_id}')
        try:
            product = cls.query.get(_id)
        except DataError:
            raise InvalidProductId
        return product




