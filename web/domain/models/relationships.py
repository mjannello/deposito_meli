from web.db import db


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
        stored_product = cls.get_product_in_location(product, location, storage)
        if not stored_product:
            stored_product = cls(product=product, location=location, storage=storage, quantity=quantity)
        else:
            stored_product.quantity += quantity
        stored_product.save()
        return stored_product.product.id

    @classmethod
    def get_all_products_in_location(cls, storage, location):
        return cls.query.filter_by(location=location, storage=storage).all()

    @classmethod
    def get_product_in_location(cls, product, location, storage):
        return cls.query.filter_by(product=product, location=location, storage=storage).first()

    @classmethod
    def remove(cls, stored_product, removal_quantity):
        stored_product.quantity -= removal_quantity
        stored_product.save()
        return stored_product.product.id

    def save(self):
        db.session.add(self)
        db.session.commit()
