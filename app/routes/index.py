from flask import Blueprint, render_template
index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    """Menampilkan halaman utama Financial Tracker"""
    return render_template('index.html')