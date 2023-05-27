import os
import threading
from flask import Flask, g
from myapp.views.deals import deals
from myapp.views.investors import investors
from myapp.views.acquisitions import acquisitions
from myapp.views.people import people
from myapp.views.company import company
from flask_swagger_ui import get_swaggerui_blueprint
from myapp.mysql_connection import MySQL
from flask_cors import CORS


def create_app():
    app = Flask(__name__,)
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)


    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # mysql connection details
    app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST', 'digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
    app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT', 25060)
    app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
    app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']
    app.config['MYSQL_CONNECT_TIMEOUT'] = 20
    


    # create MySQL instance and assign it to app.config
    mysql = MySQL(app)
    app.config['MYSQL'] = mysql


    swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Digest Africa API"
    },)



    # register the blueprint
    app.register_blueprint(deals)
    app.register_blueprint(investors)
    app.register_blueprint(acquisitions)
    app.register_blueprint(company)
    app.register_blueprint(people)
    app.register_blueprint(swaggerui_blueprint)

    return app

def get_db(app):
    if 'db' not in g:
        mysql = app.config['MYSQL']
        g.db = mysql.db
    return g.db

def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def connect_to_db(app):
    with app.app_context():
        db = get_db(app)
#         Perform your database operations



if __name__ == '__main__':
    app = create_app()

     # Create a separate thread for database connection
    db_thread = threading.Thread(target=connect_to_db, args=(app,))
    db_thread.start()

    # Run the Flask application in the main thread
    app.run(debug=True)

