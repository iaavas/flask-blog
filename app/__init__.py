from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.blog_routes import blog_bp
    from app.pages.page_routes import page_bp
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(blog_bp, url_prefix='/api/blogs')
    app.register_blueprint(page_bp, url_prefix='/')

    return app
