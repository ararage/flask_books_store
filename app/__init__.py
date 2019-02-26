# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():  # dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', '{}.py'.format(os.environ['ENVIRONMENT']))
    app.config.from_pyfile(configuration)
    db.init_app(app)    # bind database to flask app
    bootstrap.init_app(app)     # initialize bootstrap
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main  # import blueprint
    app.register_blueprint(main)  # register blueprint

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
