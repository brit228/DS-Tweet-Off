from flask import Flask, request
from .models import DB


def create_app():
    """Create instance of Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route("/")
    def home():
        user = request.args.get('user')
        return "Hello, {}!".format(user)

    return app
