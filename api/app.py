import os
import threading
from flask import Flask, g
from myapp.views.deals import deals
from myapp.views.investors import investors
from myapp.swagger import swagger_bp, swagger_blueprint

from myapp.mysql_connection import MySQL
from flask_cors import CORS


def create_app():
    # app = Flask(__name__, template_folder='./swagger/templates')
    app = Flask(__name__)
    # swagger = Swagger(swagger_bp, template_file='swagger.yml')

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # mysql connection details
    app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST', 'digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
    app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT', 25060)
    app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
    app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']
    app.config['MYSQL_CONNECT_TIMEOUT'] = 20
    # connect_timeout=timeout.total_seconds()
    


    # create MySQL instance and assign it to app.config
    mysql = MySQL(app)
    app.config['MYSQL'] = mysql

    # register the blueprint
    app.register_blueprint(deals)
    app.register_blueprint(investors)
    app.register_blueprint(swagger_bp)
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

    # app.register_blueprint(swagger_bp)


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

# import os
# import threading
# from flask import Flask, g
# from myapp.views.deals import deals
# from myapp.views.investors import investors
# from myapp.mysql_connection import MySQL
# from flask_cors import CORS

# class MyService:
#     def __init__(self, mysql):
#         self.mysql = mysql
#         # Additional initialization code for your service

#     # Define methods and functionality for your service

# def create_app():
#     app = Flask(__name__)

#     cors = CORS(app)
#     app.config['CORS_HEADERS'] = 'Content-Type'

#     # mysql connection details
#     app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST', 'digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
#     app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT', 25060)
#     app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
#     app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']
#     app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']
#     app.config['MYSQL_CONNECT_TIMEOUT'] = 20

#     # Create an instance of the MySQL class
#     mysql = MySQL(app)

#     # Instantiate the MyService class using the mysql instance
#     service = MyService(mysql)

#     # Attach the service object to the app context
#     app.config['SERVICE'] = service

#     return app


# def get_db(app):
#     if 'db' not in g:
#         mysql = app.config['MYSQL']
#         g.db = mysql.db
#     return g.db


# def close_db(error):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()


# def connect_to_db(app):
#     with app.app_context():
#         db = get_db(app)
#         # Perform your database operations using the service object
#         service = app.config['SERVICE']
#         # Use the service object to perform database operations


# if __name__ == '__main__':
#     app = create_app()

#     # Create a separate thread for database connection
#     def db_thread_function():
#         with app.app_context():
#             # Connect to the database and perform operations using the service object
#             connect_to_db(app)

#     db_thread = threading.Thread(target=db_thread_function)
#     db_thread.start()

#     # Run the Flask application in the main thread
#     app.run(debug=True)
