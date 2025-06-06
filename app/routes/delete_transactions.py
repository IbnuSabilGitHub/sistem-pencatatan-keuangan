from flask import Blueprint, jsonify
from mysql.connector import Error
from app.database.db_connection import db_connection

delete_transactions_bp = Blueprint('delete_transactions', __name__)

@delete_transactions_bp.route('/api/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transactions(transaction_id):
    """Menghapus transaksi berdasarkan ID"""
    connection = db_connection()
    if connection is None:
        return jsonify({'error': 'Koneksi database gagal'}), 500
    
    
    try:
        with connection.cursor() as cursor:
            # Cek apakah transaksi ada
            cursor.execute("SELECT id FROM transaksi WHERE id = %s", (transaction_id,))
            if cursor.fetchone() is None:
                return jsonify({'error': 'Data transaksi tidak ditemukan'}), 404
            
            # Hapus transaksi
            cursor.execute("DELETE FROM transaksi WHERE id = %s", (transaction_id,))
            connection.commit()
        
        return jsonify({'message': 'Transaksi berhasil dihapus'})
        
    except Error as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()