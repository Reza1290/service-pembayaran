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
    
    # app.config['DB_HOST'] = os.environ.get('DB_HOST')
    # app.config['DB_USER'] = os.environ.get('DB_USER')
    # app.config['DB_PASSWORD'] = os.environ.get('DB_PASSWORD')
    # app.config['DB_NAME'] = os.environ.get('DB_NAME')

    
    # # Create a MySQL connection
    # def create_connection():
    #     return pymysql.connect(
    #         host=app.config['DB_HOST'],
    #         user=app.config['DB_USER'],
    #         password=app.config['DB_PASSWORD'],
    #         db=app.config['DB_NAME'],
    #         charset='utf8mb4',
    #         cursorclass=pymysql.cursors.DictCursor
    #     )
    app.config['JSON_SORT_KEYS'] = False
    app.json.sort_keys = False


    app.config.update(**config)
    # Register Routes through the Home Blueprint
    app.register_blueprint(home)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    # Register CLI COMMANDS
    create_cli(app)
    
    return app  