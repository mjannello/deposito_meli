from web.domain.errors import InvalidArea
from web.infrastructure.db import db


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(80), nullable=False)
    hall = db.Column(db.Integer, nullable=False)
    row = db.Column(db.Integer, nullable=False)
    side = db.Column(db.String(80), nullable=False)

    location_initials = {
        'AL': 'Almacen',
        'LM': 'Limpieza',
        'SG': 'Seguridad'
    }

    @classmethod
    def parse(cls, location_str):
        area, hall, row, side = location_str.split('-')
        if area not in Location.location_initials:
            raise InvalidArea

        # the other params were validated on schemas
        area = Location.location_initials[area]
        hall = int(hall)
        row = int(row)
        side = 'izquierda' if side == 'IZ' else 'derecha'

        location = Location.query.filter_by(area=area, hall=hall, row=row, side=side).first()
        return location
