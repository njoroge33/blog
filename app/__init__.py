from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from app.main import main

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(main)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)


    return app