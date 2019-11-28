from flask import Flask
from config import config_options
from app.main import main

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(main)

    app.config.from_object(config_options[config_name])


    return app