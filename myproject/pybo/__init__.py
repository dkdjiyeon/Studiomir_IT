from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models
    from .views import (
        main_views,
        schedule_views,
        question_views,
        answer_views,
        auth_views,
        equipment_views,
        person_views,
        license_views,
        ip_views,
        admin_views,
    )

    # 블루프린트
    app.register_blueprint(main_views.bp)
    app.register_blueprint(schedule_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(equipment_views.bp)
    app.register_blueprint(person_views.bp)
    app.register_blueprint(license_views.bp)
    app.register_blueprint(ip_views.bp)
    app.register_blueprint(admin_views.bp)

    # 필터
    from .filter import formate_datetime
    app.jinja_env.filters["datetime"] = formate_datetime

    return app
