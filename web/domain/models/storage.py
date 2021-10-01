from web.db import db


class Storage(db.Model):
    __tablename__ = 'storages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    product_locations = db.relationship('ProductLocations', back_populates='storage')
