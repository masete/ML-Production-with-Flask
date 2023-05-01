from flask import Flask

from api.views.user import user_blueprint as user_blueprint
# from api.views.orders import parcel_blueprint as parcel_blueprint
from api.views.acquisitions import aquisitions_blueprint as aquisitions_blueprint


def create_app():

    app = Flask(__name__)

    # app.config['JWT_SECRET_KEY'] = 'masete'
    # JWTManager(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(parcel_blueprint)

    return app