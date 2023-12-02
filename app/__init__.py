import flask
import pymysql
import os
from cli import create_cli
from controllers import home
from config import config
from flask_cors import CORS


def create_app(name):
    # Create APP Object
    app = flask.Flask(name)
    CORS(app)
    app.config['JSON_SORT_KEYS'] = False
    app.json.sort_keys = False


    app.config.update(**config)
    # Register Routes through the Home Blueprint
    app.register_blueprint(home)
    
    
    # Register CLI COMMANDS
    create_cli(app)
    
    return app  