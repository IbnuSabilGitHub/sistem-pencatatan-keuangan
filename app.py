# from flask import render_template
# from flask import Flask
# from flask import jsonify
# from pymysql import MySQLError, OperationalError
# import pymysql
# from datetime import datetime
# import locale
# app = Flask(__name__)


# locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')


# @app.route('/')
# def index():
#     transactions_by_date = [
#         {
#             "date": '2025-05-18',
#             "type": "expense",
#             "category": "Makanan",
#             "amount": 55000,
#         },
#         {
#             "date": '2025-05-18',
#             "type": "income",
#             "category": "Tunai",
#             "note": "Gaji",
#             "amount": 20000,
#         },
#         {
#             "date": '2025-05-17',
#             "type": "expense",
#             "category": "Minum",
#             "note": "Teh",
#             "amount": 10000,
#         },
#         {
#             "date": '2025-05-16',
#             "type": "expense",
#             "category": "Makan",
#             "note": "Nasi Goreng",
#             "amount": 15000,
#         },
#         {
#             "date": '2025-05-16',
#             "type": "income",
#             "category": "Tunai",
#             "note": "-",
#             "amount": 3245,
            
#         },
#         {
#             "date": '2025-05-16',
#             "type": "income",
#             "category": "Tunai",
#             "note": "-",
#             "amount": 200000,
            
#         },
#         {
#             "date": '2025-05-16',
#             "type": "expense",
#             "category": "Minum",
#             "note": "-",
#             "amount": 10000,
            
#         }
#     ]
#     return render_template("index.html", transactions_by_date=transactions_by_date)

# BULAN_INDONESIA = [
#     "Januari", "Februari", "Maret", "April", "Mei", "Juni",
#     "Juli", "Agustus", "September", "Oktober", "November", "Desember"
# ]

# @app.context_processor
# def inject_functions():
#     def format_tanggal(tanggal_str):
#         tanggal_dt = datetime.strptime(tanggal_str, "%Y-%m-%d")
#         nama_bulan = BULAN_INDONESIA[tanggal_dt.month - 1]
#         return f"{nama_bulan} {tanggal_dt.day}"

#     def get_day_label(date_input):
#         if isinstance(date_input, str):
#             date_input = datetime.strptime(date_input, "%Y-%m-%d")
#         return date_input.strftime("%A")
    
#     # def format_currency(value):
#     #     return f"{value:,.0f}".replace(",", ".")
    
#     def format_currency(value):
#         return f"Rp {value:,.2f}"

#     return dict(format_tanggal=format_tanggal, get_day_label=get_day_label, format_currency=format_currency)

# @app.route('/api/data') # Endpoint API /api/data
# def get_data(): # Fungsi untuk mengembalikan data JSON
#     return jsonify({"message": "HELLLLLLL NAHHHH!"}) 

# if __name__ == '__main__': # Untuk menjalankan aplikasi
#     app.run(debug=True) # Set debug=True untuk mode pengembangan. agar aplikasi dapat dimuat ulang secara otomatis saat ada perubahan pada kode.