import os
from flask import Flask
from myapp.views.deals import deals
from myapp.mysql_connection import MySQL

def create_app():
    app = Flask(__name__)

    # mysql connection details
    app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST', 'digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
    app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT', 25060)
    app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
    app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']

    # create MySQL instance and assign it to app.config
    mysql = MySQL(app)
    app.config['MYSQL'] = mysql

    # register the blueprint
    app.register_blueprint(deals)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
