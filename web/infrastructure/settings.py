import os

DB_USER = os.environ.get('DB_USER', 'meli_admin')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '1234')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_SEED_EXECUTION = os.environ.get('EXECUTE_DB_SEED', True)
