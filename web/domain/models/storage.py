from web.domain.models.db import db


class Storage(db.Model):
    __tablename__ = 'storages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    stored_products = db.relationship('StoredProducts', back_populates='storage')

    @classmethod
    def get_storage(cls, storage_name):
        return cls.query.filter_by(name=storage_name).first()
