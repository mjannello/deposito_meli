from flask import Flask
# from flask_migrate import Migrate
from web.db import db
from web.api import api
from web.domain.models.location import Location
from web.domain.models.product import Product
from web.domain.models.relationships import StoredProducts
from web.domain.models.storage import Storage
from web.views.products_views import ns_products

app = Flask(__name__)
# migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meli_admin:1234@localhost/meli_storage'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db.init_app(app)
api.init_app(app)
api.add_namespace(ns_products)


def db_seed():
    product1 = Product(id=1, name='nombre 1', type='tipo1')
    product2 = Product(id=2, name='nombre 1', type='tipo2')
    product3 = Product(id=3, name='nombre 1', type='tipo3')

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)

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

    # location1.products.append(product1)
    # stg.locations.append(location1)

    # db.session.add(stg)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        db_seed()
        p = Product(id=4, name='nombre 1', type='tipo4')
        loc = Location(area='Limpieza', hall=4, row=2, side='derecha')
        stg = Storage(id=2, name='BR02')

        product_location = StoredProducts(product=p, location=loc, storage=stg, quantity=10)
        db.session.add(product_location)
        db.session.commit()

    app.run()
