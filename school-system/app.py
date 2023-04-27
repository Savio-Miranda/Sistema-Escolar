from flask import Flask
from sistema import views


def create_app(test_config=None):
    app = Flask(__name__)
    views.init_app(app)

    return app