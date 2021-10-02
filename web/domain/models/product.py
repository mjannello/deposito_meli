import logging
from web.db import db


logger = logging.getLogger(__name__)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    product_locations = db.relationship('ProductLocations', back_populates='product')

    @classmethod
    def find_by_id(cls, _id):
        logger.debug(f'Find product by id: {_id}')
        product = cls.query.get(_id)
        return product




