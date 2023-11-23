from flask import Blueprint, jsonify
from db import connect

home = Blueprint('home', __name__)

@home.route('/')
def home_home():
    return "Hi!"


@home.route('/keuangan')
def get_all_keuangan():
    
    try:
        with connect.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM keuangans')
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        connection.close()
    