from flask import Flask
from flask_cors import CORS, cross_origin
import jwt
from .db import DB


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "004f2af45d3a4e161a7dd2d17fdae47f"
    cors = CORS(app)

    with app.app_context():
        app.db = DB
        from server.user.user import user_bp
        from server.tiers.tiers import tiers_bp
        from server.checkout.checkout import checkout_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(tiers_bp)
        app.register_blueprint(checkout_bp)

        return app
