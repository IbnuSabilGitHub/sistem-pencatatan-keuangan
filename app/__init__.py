from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes.index import index_bp
    app.register_blueprint(index_bp, url_prefix='/')
    return app