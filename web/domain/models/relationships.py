from web.db import db


class ProductLocations(db.Model):
    __tablename__ = 'product_locations'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    storaged_id = db.Column(db.Integer, db.ForeignKey('storages.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    __table_args__ = (db.UniqueConstraint(product_id, location_id, storaged_id), )

    product = db.relationship('Product', back_populates='product_locations')
    location = db.relationship('Location')
    storage = db.relationship('Storage', back_populates='product_locations')

    def save(self):
        db.session.add(self)
        db.session.commit()
