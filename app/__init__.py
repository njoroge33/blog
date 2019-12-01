from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
import arrow

bootstrap = Bootstrap()
db = SQLAlchemy()
login = LoginManager()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    bootstrap.init_app(app)
    db.init_app(app)
    login.init_app(app)
    configure_uploads(app,photos)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    def format_date(value):
        dt = arrow.get(value).to('UTC+3')
        return arrow.get(dt).humanize()


    app.jinja_env.filters['timeago'] = format_date

    return app