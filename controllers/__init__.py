from flask import Blueprint, jsonify, json
from .db import connect
from flask import request
from datetime import datetime


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
            

@home.route('/invoices',methods=['GET'])
def get_all_invoices():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM invoices')
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()
            
@home.route('/invoices/<int:id>', methods=['GET'])
def get_invoices_by_id(id):
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM invoices WHERE id=%s', (id,))
            result = cursor.fetchone()

            if result:
                return jsonify(result)
            else:
                return jsonify({'error': f'Invoices with id {id} not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()

@home.route('/invoices', methods=['POST'])
def create_invoices():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            data = request.json

            
            if 'id_detail_kunjungan' not in data:
                return jsonify({'error': 'Invalid data format'}), 400
            if 'catatan' not in data:
                data['catatan']= ''
            if 'receipt_file_path' not in data:
                data['receipt_file_path'] = ''

            cursor.execute('INSERT INTO invoices (id_detail_kunjungan, catatan, receipt_file_path) VALUES (%s, %s, %s)',
                           (data['id_detail_kunjungan'], data['catatan'], data['receipt_file_path'] ))
            connection.commit()
            return jsonify({'message': 'Keuangan created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()


@home.route('/invoices/<int:id>', methods=['PUT'])
def update_invoices(id):
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            data = request.json

            
            if 'id_detail_kunjungan' not in data:
                return jsonify({'error': 'Invalid data format'}), 400

            cursor.execute('UPDATE invoices SET id_detail_kunjungan=%s, catatan=%s, receipt_file_path=%s WHERE id=%s',
                           (data['id_detail_kunjungan'], data['catatan'], data['receipt_file_path'], id))
            connection.commit()
            return jsonify({'message': f'Keuangan with id {id} updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()

@home.route('/invoices/<int:id>', methods=['DELETE'])
def delete_invoices(id):
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('DELETE FROM invoices WHERE id=%s', (id,))
            connection.commit()
            return jsonify({'message': f'Invoices with id {id} deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()
 
 
def get_all_detail_kunjungans():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM detail_kunjungans')
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()

def get_all_kunjungans():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM kunjungans')
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            connection.close()
 
@home.route('/pembayaran/ringkasan', methods=['GET'])
def pembayaran_ringkasan():
    data = {
        "status" : True,
        "data": {}
    }
    
    entry = data["data"]
    
    response = get_all_keuangan()
    
    keuangan_json = response.get_data(as_text=True)
    
    keuangan = json.loads(keuangan_json)
    
    total_income = 0
    total_outcome = 0
    income_month = [0] * 12
    outcome_month = [0] * 12
    
    
    current_year = datetime.now().year 
    
    for entry_data in keuangan:
        tanggal_arsip = datetime.strptime(entry_data['tanggal_arsip'], '%a, %d %b %Y %H:%M:%S %Z')
        
        if tanggal_arsip.year == current_year and 1 <= tanggal_arsip.month <= 12:
            month_index = tanggal_arsip.month - 1 
            income_month[month_index] += entry_data['pemasukan']
            outcome_month[month_index] += entry_data['pengeluaran']

        if tanggal_arsip.year == current_year:
            total_income += entry_data['pemasukan']
            total_outcome += entry_data['pengeluaran']
    
    entry['total_income'] = total_income
    entry['total_outcome'] = total_outcome
    entry['income_month'] = income_month
    entry['outcome_month'] = outcome_month
    
    return jsonify(data)
    
    

@home.route('/pembayaran/transaksi',methods=['GET'])
def pembayaran_transaksi():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            # query = """
            #     SELECT * FROM invoices
            #     LEFT JOIN detail_kunjungans ON invoices.id_detail_kunjungan = detail_kunjungans.id
            #     LEFT JOIN kunjungans ON detail_kunjungans.kunjungan_id = kunjungans.id
            #     LEFT JOIN pasiens ON kunjungans.pasien_id = pasiens.id
            #     LEFT JOIN prescriptions ON detail_kunjungans.apotek_id = prescriptions.id
            #     LEFT JOIN prescription_details ON prescriptions.id = prescription_details.prescription_id
            #     LEFT JOIN result_labs ON kunjungans.id = result_labs.kunjungan_id
            #     LEFT JOIN labs ON result_labs.lab_id = labs.id
            #     LEFT JOIN drugs ON prescription_details.drug_id = drugs.id
                
            #     WHERE kunjungans.status_pembayaran = 0
                
            # """
            
            # cursor.execute(query)
            # invoices = cursor.fetchall()
            # return jsonify(invoices)
            
            data = []

            query_invoices = """
                SELECT invoices.* FROM invoices
                LEFT JOIN detail_kunjungans ON invoices.id_detail_kunjungan = detail_kunjungans.id
                LEFT JOIN kunjungans ON detail_kunjungans.kunjungan_id = kunjungans.id
                WHERE kunjungans.status_pembayaran = 0
            """

            cursor.execute(query_invoices)
            invoices = cursor.fetchall()

            
            for invoice in invoices:
                invoice_data = json.loads((jsonify(invoice)).get_data(as_text=True))
                
                
                query_detail_kunjungans = f"""
                    SELECT * FROM detail_kunjungans
                    WHERE id = {invoice['id_detail_kunjungan']}
                """
                
                cursor.execute(query_detail_kunjungans)
                detail_kunjungan = cursor.fetchone()  

                if detail_kunjungan:
                    
                    invoice_data['detail_kunjungan'] = json.loads((jsonify(detail_kunjungan)).get_data(as_text=True))

                    
                    query_kunjungan = f"""
                        SELECT * FROM kunjungans
                        WHERE id = {detail_kunjungan['kunjungan_id']}
                    """
                    
                    cursor.execute(query_kunjungan)
                    kunjungan = cursor.fetchone()  

                    if kunjungan:
                        #
                        invoice_data['kunjungan'] = json.loads((jsonify(kunjungan)).get_data(as_text=True))
                        
                        query_pasien = f"""
                            SELECT * FROM pasiens
                            WHERE id = {kunjungan['pasien_id']}
                        """
                        
                        cursor.execute(query_pasien)
                        pasien = cursor.fetchone()
                        
                        if pasien:
                            
                            invoice_data['pasien'] = json.loads((jsonify(pasien)).get_data(as_text=True))
                            
                    if detail_kunjungan['apotek_id'] != None:
                        query_resep = f"""
                            SELECT * FROM prescriptions
                            WHERE id = {detail_kunjungan['apotek_id']}
                        """
                        
                        cursor.execute(query_resep)
                        resep = cursor.fetchone()
                            
                        if resep:
                            invoice_data['resep'] = json.loads((jsonify(resep)).get_data(as_text=True))    
                        
                            query_detail_resep = f"""
                            SELECT * FROM prescription_details
                            WHERE prescription_id = {resep['id']}
                            """
                            
                            cursor.execute(query_detail_resep)
                            detail_resep = cursor.fetchall()
                            
                            if detail_resep:
                                x = invoice_data['resep']['detail_resep'] = []
                                
                                
                                for i in detail_resep:
                                    y = json.loads((jsonify(i)).get_data(as_text=True))
                                    
                                    
                                    query_obat = f"""
                                    SELECT * FROM drugs
                                    WHERE id = {i['drug_id']}
                                    """
                                    
                                    cursor.execute(query_obat)
                                    obat = cursor.fetchone()
                                    
                                    if obat:
                                        y['detail_obat'] = json.loads((jsonify(obat)).get_data(as_text=True))
                                        
                                    x.append(y)

                    query_res_labs = f"""
                    SELECT * FROM result_labs
                    WHERE kunjungan_id = {kunjungan['id']}
                    """

                    cursor.execute(query_res_labs)
                    res_labs = cursor.fetchall()
                    
                    if res_labs:
                        x = invoice_data['result_lab'] = []
                        
                        for i in res_labs:
                            y = json.loads((jsonify(i).get_data(as_text=True)))
                            
                            query_labs = f"""
                            SELECT * FROM labs
                            WHERE id = {i['lab_id']}
                            """

                            cursor.execute(query_labs)
                            lab = cursor.fetchone()
                            
                            if lab:
                                y['lab'] = json.loads((jsonify(lab).get_data(as_text=True)))
                            
                            query_pegawai_lab = f"""
                            SELECT name,roles,no_pegawai FROM users
                            WHERE id = {i['user_id']}
                            """
                            
                            cursor.execute(query_pegawai_lab)
                            pegawai_lab = cursor.fetchone()
                            
                            if pegawai_lab:
                                y['pegawai_lab'] = json.loads((jsonify(pegawai_lab).get_data(as_text=True)))
                            
                            x.append(y)

                            
               
                data.append(invoice_data)
                
            # return json.dumps(data, indent=2, sort_keys=False)
            return jsonify(data)    
    finally:
        connection.close()
    
    
@home.route('/pembayaran/riwayat',methods=['GET'])
def pembayaran_riwayat():
    connection = None
    try:
        connection = connect()
        with connection.cursor(dictionary=True) as cursor:
            
            data = []

            query_invoices = """
                SELECT invoices.* FROM invoices
                LEFT JOIN detail_kunjungans ON invoices.id_detail_kunjungan = detail_kunjungans.id
                LEFT JOIN kunjungans ON detail_kunjungans.kunjungan_id = kunjungans.id
                WHERE kunjungans.status_pembayaran = 1
            """

            cursor.execute(query_invoices)
            invoices = cursor.fetchall()

            
            for invoice in invoices:
                invoice_data = json.loads((jsonify(invoice)).get_data(as_text=True))
                
                
                query_detail_kunjungans = f"""
                    SELECT * FROM detail_kunjungans
                    WHERE id = {invoice['id_detail_kunjungan']}
                """
                
                cursor.execute(query_detail_kunjungans)
                detail_kunjungan = cursor.fetchone()  

                if detail_kunjungan:
                    
                    invoice_data['detail_kunjungan'] = json.loads((jsonify(detail_kunjungan)).get_data(as_text=True))

                    
                    query_kunjungan = f"""
                        SELECT * FROM kunjungans
                        WHERE id = {detail_kunjungan['kunjungan_id']}
                    """
                    
                    cursor.execute(query_kunjungan)
                    kunjungan = cursor.fetchone()  

                    if kunjungan:
                        #
                        invoice_data['kunjungan'] = json.loads((jsonify(kunjungan)).get_data(as_text=True))
                        
                        query_pasien = f"""
                            SELECT * FROM pasiens
                            WHERE id = {kunjungan['pasien_id']}
                        """
                        
                        cursor.execute(query_pasien)
                        pasien = cursor.fetchone()
                        
                        if pasien:
                            
                            invoice_data['pasien'] = json.loads((jsonify(pasien)).get_data(as_text=True))
                            
                    if detail_kunjungan['apotek_id'] != None:
                        query_resep = f"""
                            SELECT * FROM prescriptions
                            WHERE id = {detail_kunjungan['apotek_id']}
                        """
                        
                        cursor.execute(query_resep)
                        resep = cursor.fetchone()
                            
                        if resep:
                            invoice_data['resep'] = json.loads((jsonify(resep)).get_data(as_text=True))    
                        
                            query_detail_resep = f"""
                            SELECT * FROM prescription_details
                            WHERE prescription_id = {resep['id']}
                            """
                            
                            cursor.execute(query_detail_resep)
                            detail_resep = cursor.fetchall()
                            
                            if detail_resep:
                                x = invoice_data['resep']['detail_resep'] = []
                                
                                
                                for i in detail_resep:
                                    y = json.loads((jsonify(i)).get_data(as_text=True))
                                    
                                    
                                    query_obat = f"""
                                    SELECT * FROM drugs
                                    WHERE id = {i['drug_id']}
                                    """
                                    
                                    cursor.execute(query_obat)
                                    obat = cursor.fetchone()
                                    
                                    if obat:
                                        y['detail_obat'] = json.loads((jsonify(obat)).get_data(as_text=True))
                                        
                                    x.append(y)

                    query_res_labs = f"""
                    SELECT * FROM result_labs
                    WHERE kunjungan_id = {kunjungan['id']}
                    """

                    cursor.execute(query_res_labs)
                    res_labs = cursor.fetchall()
                    
                    if res_labs:
                        x = invoice_data['result_lab'] = []
                        
                        for i in res_labs:
                            y = json.loads((jsonify(i).get_data(as_text=True)))
                            
                            query_labs = f"""
                            SELECT * FROM labs
                            WHERE id = {i['lab_id']}
                            """

                            cursor.execute(query_labs)
                            lab = cursor.fetchone()
                            
                            if lab:
                                y['lab'] = json.loads((jsonify(lab).get_data(as_text=True)))
                            
                            query_pegawai_lab = f"""
                            SELECT name,roles,no_pegawai FROM users
                            WHERE id = {i['user_id']}
                            """
                            
                            cursor.execute(query_pegawai_lab)
                            pegawai_lab = cursor.fetchone()
                            
                            if pegawai_lab:
                                y['pegawai_lab'] = json.loads((jsonify(pegawai_lab).get_data(as_text=True)))
                            
                            x.append(y)

                            
               
                data.append(invoice_data)
                
            # return json.dumps(data, indent=2, sort_keys=False)
            return jsonify(data)    
    finally:
        connection.close()
    
    
    
    
    