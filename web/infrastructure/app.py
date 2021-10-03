from flask import Flask
from web.infrastructure.db import db
from web.infrastructure.api import api
from web.domain.models.location import Location
from web.domain.models.product import Product
from web.domain.models.storage import Storage
from web.infrastructure.views.location_views import ns_locations
from web.infrastructure.views.products_views import ns_products
from web.infrastructure.views.search_views import ns_search

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meli_admin:1234@localhost/meli_storage'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db.init_app(app)
api.init_app(app)
api.add_namespace(ns_products)
api.add_namespace(ns_locations)
api.add_namespace(ns_search)


def db_seed():
    product1 = Product(id=1, name='nombre 1', type='tipo1')
    product2 = Product(id=2, name='nombre 2', type='tipo2')
    product3 = Product(id=3, name='nombre 3', type='tipo3')
    product4 = Product(id=4, name='nombre 4', type='tipo4')
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)

    areas = ['Limpieza', 'Almacen', 'Seguridad']

    #row 0 Limpieza
    location1 = Location(area=areas[0], hall=0, row=0, side='izquierda')
    db.session.add(location1)

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

    stg = Storage(id=1, name='AR01')
    db.session.add(stg)

    db.session.add(Storage(id=2, name='BR02'))
    db.session.add(Storage(id=3, name='CO03'))

    # location1.products.append(product1)
    # stg.locations.append(location1)

    # db.session.add(stg)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        db_seed()

    app.run()
