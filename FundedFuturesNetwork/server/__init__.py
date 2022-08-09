from flask import Flask
from flask_cors import CORS, cross_origin
from .db import DB

def create_app():
    app = Flask(__name__)
    cors = CORS(app)

    with app.app_context():
        app.db = DB
        from server.user.user import user_bp
        from server.tiers.tiers import tiers_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(tiers_bp)

        return app
