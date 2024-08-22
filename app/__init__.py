from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager
from .routes.shop import bp as shop_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(shop_bp)

    # Custom Error Handlers
    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f'Server Error: {error}')
        return render_template('500.html'), 500

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('403.html'), 403
