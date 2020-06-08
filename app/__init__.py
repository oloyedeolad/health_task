from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Import the configurations
from instance.config import app_config

application = Flask(
        import_name="app",
        template_folder="templates",
        static_folder='static',
        instance_relative_config=True)

database = SQLAlchemy(application)

def create_app(config_name):
    application.config.from_object(app_config[config_name])
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(application)
    bootstrap = Bootstrap(application)
    migrate = Migrate(app = application, db = database, directory="intron_health_migrations")

    register_blueprints()

    return application


"""
 The following registers the Blueprints with the application.
"""
def register_blueprints():
    # Import all BluePrints
    from .home import home as home_blueprint
    from .hmo import hmo as hmo_blueprint
    application.register_blueprint(home_blueprint, url_prefix='/home')
    application.register_blueprint(hmo_blueprint, url_prefix='/hmo')