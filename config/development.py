import os

user_connection = os.environ['LEXICON_DATABASE_USER']
password_connection = os.environ['LEXICON_DATABASE_PASSWORD']
host_connection = os.environ['LEXICON_DATABASE_HOST']
port_connection = os.environ['LEXICON_DATABASE_PORT']
database = os.environ['LEXICON_DATABASE']
SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['ALCHEMY_TRACK']
DEBUG = os.environ['FLASK_DEBUG']

SQLALCHEMY_DATABASE_URI = 'postgres://{user_connection}:{password_connection}@{host_connection}:{port_connection}/{database}'\
    .format(user_connection=user_connection, password_connection=password_connection, host_connection=host_connection,
            port_connection=port_connection, database=database)
