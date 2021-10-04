from flask import Flask
from web.domain.models.db import db
from web.infrastructure.api import api
from web.domain.models.location import Location
from web.domain.models.product import Product
from web.domain.models.storage import Storage
from web.infrastructure.settings import DB_SEED_EXECUTION, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from web.infrastructure.views.location_views import ns_locations
from web.infrastructure.views.products_views import ns_products
from web.infrastructure.views.search_views import ns_search

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/meli_storage'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
api.init_app(app)
api.add_namespace(ns_products)
api.add_namespace(ns_locations)
api.add_namespace(ns_search)


def db_seed():
    for i in range(1, 100):
        p = Product(id=i, name=f'nombre {i}', type=f'type {i}')
        db.session.add(p)

    areas = ['Limpieza', 'Almacen', 'Seguridad']
    '''
    Same example showed in the exercise PDF. This could be programmed automatically taking into consideration the limits 
    of every location area and fill in the matrix of halls and rows. As it is a DB seed data, and the existance of the
    location is not being validated, I preferred not doing so.
    '''

    #row 0 Limpieza
    db.session.add(Location(area=areas[0], hall=0, row=0, side='izquierda'))
    db.session.add(Location(area=areas[0], hall=1, row=0, side='izquierda'))
    db.session.add(Location(area=areas[0], hall=1, row=0, side='derecha'))
    db.session.add(Location(area=areas[0], hall=2, row=0, side='derecha'))

    # row 1 Limpieza
    db.session.add(Location(area=areas[0], hall=0, row=1, side='izquierda'))
    db.session.add(Location(area=areas[0], hall=1, row=1, side='izquierda'))
    db.session.add(Location(area=areas[0], hall=1, row=1, side='derecha'))
    db.session.add(Location(area=areas[0], hall=2, row=1, side='derecha'))
    # row 0 Almacen
    db.session.add(Location(area=areas[1], hall=2, row=0, side='izquierda'))
    db.session.add(Location(area=areas[1], hall=3, row=0, side='izquierda'))
    db.session.add(Location(area=areas[1], hall=3, row=0, side='derecha'))
    db.session.add(Location(area=areas[1], hall=4, row=0, side='derecha'))
    # row 1 Almacen
    db.session.add(Location(area=areas[1], hall=2, row=1, side='izquierda'))
    db.session.add(Location(area=areas[1], hall=3, row=1, side='izquierda'))
    db.session.add(Location(area=areas[1], hall=3, row=1, side='derecha'))
    db.session.add(Location(area=areas[1], hall=4, row=1, side='derecha'))

    # row 2 Almacen
    db.session.add(Location(area=areas[1], hall=2, row=2, side='izquierda'))
    db.session.add(Location(area=areas[1], hall=3, row=2, side='izquierda'))
    db.session.add(Location(area=areas[1], hall=3, row=2, side='derecha'))
    db.session.add(Location(area=areas[1], hall=4, row=2, side='derecha'))

    # row 2 Seguridad
    db.session.add(Location(area=areas[2], hall=0, row=2, side='izquierda'))
    db.session.add(Location(area=areas[2], hall=1, row=2, side='izquierda'))
    db.session.add(Location(area=areas[2], hall=1, row=2, side='derecha'))
    db.session.add(Location(area=areas[2], hall=2, row=2, side='derecha'))

    db.session.add(Storage(id=1, name='AR01'))
    db.session.add(Storage(id=3, name='CO02'))
    db.session.add(Storage(id=2, name='BR05'))

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        if DB_SEED_EXECUTION:
            db_seed()

    app.run()
