from flask import Blueprint, jsonify
from .db import connect
from flask import request

home = Blueprint('home', __name__)

@home.route('/')
def home_home():
    return "Hi!"


@home.route('/keuangan', methods=['GET'])
def get_all_keuangan():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM keuangans')
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()

@home.route('/keuangan/<int:id>', methods=['GET'])
def get_keuangan_by_id(id):
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM keuangans WHERE id=%s', (id,))
            result = cursor.fetchone()

            if result:
                return jsonify(result)
            else:
                return jsonify({'error': f'Keuangan with id {id} not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()

@home.route('/keuangan', methods=['POST'])
def create_keuangan():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            data = request.json

            
            if 'tanggal_arsip' not in data or 'pemasukan' not in data or 'pengeluaran' not in data:
                return jsonify({'error': 'Invalid data format'}), 400

            cursor.execute('INSERT INTO keuangans (tanggal_arsip, pemasukan, pengeluaran) VALUES (%s, %s, %s)',
                           (data['tanggal_arsip'], data['pemasukan'], data['pengeluaran']))
            connection.commit()
            return jsonify({'message': 'Keuangan created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()


@home.route('/keuangan/<int:id>', methods=['PUT'])
def update_keuangan(id):
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            data = request.json

            
            if 'tanggal_arsip' not in data or 'pemasukan' not in data or 'pengeluaran' not in data:
                return jsonify({'error': 'Invalid data format'}), 400

            cursor.execute('UPDATE keuangans SET tanggal_arsip=%s, pemasukan=%s, pengeluaran=%s WHERE id=%s',
                           (data['tanggal_arsip'], data['pemasukan'], data['pengeluaran'], id))
            connection.commit()
            return jsonify({'message': f'Keuangan with id {id} updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()

@home.route('/keuangan/<int:id>', methods=['DELETE'])
def delete_keuangan(id):
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('DELETE FROM keuangans WHERE id=%s', (id,))
            connection.commit()
            return jsonify({'message': f'Keuangan with id {id} deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()
            
