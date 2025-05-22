import pymysql

def connect_db():
    """Connect to the database and return the connection."""
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='testing',
    )