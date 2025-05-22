from flask import Blueprint, render_template
index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    transactions_by_date = [
        {
            "date": '2025-05-18',
            "type": "expense",
            "category": "Makanan",
            "amount": 55000,
        },
        {
            "date": '2025-05-18',
            "type": "income",
            "category": "Tunai",
            "note": "Gaji",
            "amount": 20000,
        },
        {
            "date": '2025-05-17',
            "type": "expense",
            "category": "Minum",
            "note": "Teh",
            "amount": 10000,
        },
        {
            "date": '2025-05-16',
            "type": "expense",
            "category": "Makan",
            "note": "Nasi Goreng",
            "amount": 15000,
        },
        {
            "date": '2025-05-16',
            "type": "income",
            "category": "Tunai",
            "note": "-",
            "amount": 3245,
            
        },
        {
            "date": '2025-05-16',
            "type": "income",
            "category": "Tunai",
            "note": "-",
            "amount": 200000,
            
        },
        {
            "date": '2025-05-16',
            "type": "expense",
            "category": "Minum",
            "note": "-",
            "amount": 10000,
            
        }
    ]
    return render_template("index.html", transactions_by_date=transactions_by_date)
