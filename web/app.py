from flask import Flask

from web.api import api
from web.views.products_views import ns_products

app = Flask(__name__)

api.init_app(app)
api.add_namespace(ns_products)

if __name__ == '__main__':
    app.run()
