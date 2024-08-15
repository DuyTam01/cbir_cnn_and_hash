from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
# database, migrate để tự động viết kịch bản để cập nhật db dễ hơn
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view='auth.login'
bootstrap = Bootstrap()
def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    login.init_app(app=app)
    bootstrap.init_app(app=app)
    # registering blueprints
    # import chỗ này để tránh lỗi import vòng tròn
    from website.main import bp as main_bp
    app.register_blueprint(main_bp)
    from website.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from website.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    return app
from website import models