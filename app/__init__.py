# app/__init__.py
from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Registrar blueprint
    app.register_blueprint(main)

    return app
