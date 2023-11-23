import flask
import pymysql
import os
from cli import create_cli
from controllers import home
from config import config

def create_app(name):
    # Create APP Object
    app = flask.Flask(name)
    
    # Update Config Values
    app.config['DB_HOST'] = os.environ.get('DB_HOST', 'localhost')
    app.config['DB_USER'] = os.environ.get('DB_USER', 'username')
    app.config['DB_PASSWORD'] = os.environ.get('DB_PASSWORD', 'password')
    app.config['DB_NAME'] = os.environ.get('DB_NAME', 'your_database_name')

    # Create a MySQL connection
    def create_connection():
        return pymysql.connect(
            host=app.config['DB_HOST'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            db=app.config['DB_NAME'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    # Register Routes through the Home Blueprint
    app.register_blueprint(home)

    # Register CLI COMMANDS
    create_cli(app)

    return app