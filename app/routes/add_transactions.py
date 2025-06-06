from flask import Blueprint, jsonify, request
from mysql.connector import Error
from app.database.db_connection import db_connection
from datetime import datetime

add_transactions_bp = Blueprint('add_transactions', __name__)

@add_transactions_bp.route('/api/transactions', methods=['POST'])
def add_transactions():
    """Menambah transaksi baru"""
    connection = db_connection()
    if connection is None:
        return jsonify({'error': 'Koneksi database gagal'}), 500

    try:
        data = request.get_json()
        
        # Validasi field yang diperlukan
        required_fields = ['jumlah', 'id_kategori', 'tanggal']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Field {field} wajib diisi'}), 422

        # Validasi jumlah
        try:
            jumlah = float(data['jumlah'])
            if jumlah <= 0:
                return jsonify({'error': 'Jumlah harus lebih dari 0'}), 422
        except ValueError:
            return jsonify({'error': 'Format jumlah tidak valid'}), 422

        # Validasi tanggal format
        try:
            datetime.strptime(data['tanggal'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Format tanggal tidak valid. Gunakan YYYY-MM-DD'}), 422

        # Validasi id_kategori dan ambil tipe_id dari kategori
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT tipe_id FROM kategori WHERE id_kategori = %s", (data['id_kategori'],))
            kategori = cursor.fetchone()
            if not kategori:
                return jsonify({'error': 'Kategori tidak ditemukan'}), 422

        with connection.cursor() as cursor:
            query = """
                INSERT INTO transaksi (jumlah, id_kategori, deskripsi, tanggal)
                VALUES (%s, %s, %s, %s)
            """
            values = (
                jumlah,
                data['id_kategori'],
                data.get('deskripsi', ''),
                data['tanggal']
            )
            cursor.execute(query, values)
            connection.commit()

        return jsonify({
            'message': 'Transaksi berhasil ditambahkan',
        }), 201

    except Error as e:
        connection.rollback()
        return jsonify({'error': f'Terjadi kesalahan: {str(e)}'}), 500
    finally:
        connection.close()
