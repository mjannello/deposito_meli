from flask import Flask

from web.db import db
from web.api import api
from web.views.products_views import ns_products

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/meli_storage'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

api.init_app(app)
api.add_namespace(ns_products)
db.init_app(app)

if __name__ == '__main__':
    app.run()
