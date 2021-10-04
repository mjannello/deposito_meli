from flask_restplus import Api

api = Api(
    version='1.0',
    title='MeLi Storage API',
    contact_email='matijannello@gmail.com',
    description=(
        'API to manage MercadoLibre\'s storage'
    )
)
