from flask import Flask

from src.utils.errors.CustomException import CustomException

# Routes
from .routes import _ExampleRoute
from .routes import AuthRoutes
from .routes import CourtRoutes
from .routes import ModuleMenuRoutes
from .routes import ModulesRoutes
from .routes import ProfilePermissionsRoutes
from .routes import ProfileRoutes
from .routes import UserRoutes
from .routes import UserTypeRoutes
from .routes import WalletRoutes
from .routes import CustomerRoutes
from .routes import PaymentReceiptsRoute

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(_ExampleRoute.main, url_prefix='/example')
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(CourtRoutes.main,url_prefix = '/courts')
    app.register_blueprint(ModuleMenuRoutes.main, url_prefix='/module_menus')
    app.register_blueprint(ModulesRoutes.main, url_prefix='/modules')
    app.register_blueprint(ProfilePermissionsRoutes.main, url_prefix='/profile_permissions')
    app.register_blueprint(ProfileRoutes.main, url_prefix='/profiles')
    app.register_blueprint(UserRoutes.main, url_prefix='/user')
    app.register_blueprint(CustomerRoutes.main, url_prefix='/customer')
    app.register_blueprint(UserTypeRoutes.main, url_prefix='/user_types')
    app.register_blueprint(WalletRoutes.main, url_prefix='/wallet')
    app.register_blueprint(PaymentReceiptsRoute.main, url_prefix='/receipts')

    return app