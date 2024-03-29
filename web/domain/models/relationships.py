from sqlalchemy.exc import SQLAlchemyError

from web.domain.models.db import db


class StoredProducts(db.Model):
    __tablename__ = 'stored_products'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    storaged_id = db.Column(db.Integer, db.ForeignKey('storages.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    __table_args__ = (db.UniqueConstraint(product_id, location_id, storaged_id), )

    product = db.relationship('Product', back_populates='stored_products')
    location = db.relationship('Location')
    storage = db.relationship('Storage', back_populates='stored_products')

    @classmethod
    def upsert(cls, product, location, storage, quantity):
        try:
            stored_product = cls.get_product_in_location(product, location, storage)
            if not stored_product:
                stored_product = cls(product=product, location=location, storage=storage, quantity=quantity)
            else:
                stored_product.quantity += quantity
            stored_product.save()
        except SQLAlchemyError as e:
            raise e
        return stored_product.product.id

    @classmethod
    def get_all_products_in_location(cls, storage, location):
        try:
            products_in_location = cls.query.filter_by(location=location, storage=storage).all()
        except SQLAlchemyError as e:
            raise e
        return products_in_location

    @classmethod
    def get_product_in_location(cls, product, location, storage):
        try:
            product_in_location = cls.query.filter_by(product=product, location=location, storage=storage).first()
        except SQLAlchemyError as e:
            raise e
        return product_in_location

    @classmethod
    def remove(cls, stored_product, removal_quantity):
        stored_product.quantity -= removal_quantity
        if stored_product.quantity == 0:
            deleted_id = stored_product.id
            stored_product.delete()
            return deleted_id
        stored_product.save()
        return stored_product.product.id

    @classmethod
    def get_locations_in_storage(cls, storage, product):
        try:
            locations = cls.query.filter_by(product=product, storage=storage).all()
        except SQLAlchemyError as e:
            raise e
        return locations

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
