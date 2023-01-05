from flask import Flask


def create_app(settings_module='config.development'):
    app = Flask(__name__)
    app.config.from_object(settings_module)