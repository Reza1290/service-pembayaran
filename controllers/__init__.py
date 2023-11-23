from flask import Blueprint, jsonify
import mysql.connector
import os

home = Blueprint('home', __name__)

@home.route('/')
def home_home():
    return "Hi!"


@home.route('/keuangan')
def get_all_keuangan():
    # Get MySQL container connection details from environment variables
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'username')
    db_password = os.environ.get('DB_PASSWORD', 'password')
    db_name = os.environ.get('DB_NAME', 'your_database_name')

    # Establish a connection to the MySQL container
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM keuangans')
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        connection.close()
    