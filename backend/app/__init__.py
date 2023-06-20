from flask import Flask
from config import Config
# from .route.route import main
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config=Config):
    app = Flask(__name__)

    app.register_error_handler(404, page_not_found)

    app.config.from_object(config)

    from .route.route import main
    app.register_blueprint(main, url_prefix="/api/v1")

    from app import models

    db.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app

def page_not_found(error):
    return {"error": "Not found"}, 404