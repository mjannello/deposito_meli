import uuid
import logging
from sqlalchemy.dialects.postgresql import UUID
from web.db import db


logger = logging.getLogger(__name__)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(80), primary_key=True)
    type = db.Column(db.String(80), nullable=False)


class ProductStorageLocation(db.Model):
    pass