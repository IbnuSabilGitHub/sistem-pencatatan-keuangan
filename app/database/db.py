import pymysql

def connect_db():
    """Kokenksi ke database MySQL dan kembalikan objek koneksi."""
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='transaksi',
    )