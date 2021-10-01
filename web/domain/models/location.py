from web.db import db


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(80), nullable=False)
    hall = db.Column(db.Integer, nullable=False)
    row = db.Column(db.Integer, nullable=False)
    side = db.Column(db.String(80), nullable=False)

