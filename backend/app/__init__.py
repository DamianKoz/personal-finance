from flask import Flask
from config import Config
from .route.route import main


def page_not_found(error):
    return {"error": "Not found"}, 404


def create_app(config=Config):
    app = Flask(__name__)

    app.register_error_handler(404, page_not_found)

    app.config.from_object(config)

    app.register_blueprint(main, url_prefix="/api/v1")

    return app
