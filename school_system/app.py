from flask import Flask
from school_system.extensions import site


def create_app():
    app = Flask(__name__)
    site.init_app(app)

    return app

