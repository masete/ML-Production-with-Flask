import os
from flask import Flask
import MySQLdb
import threading


class MySQL:
    def __init__(self, app=None):
        self.db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not self.db:
            host = app.config['MYSQL_HOST']
            port = app.config['MYSQL_PORT']
            user = app.config['MYSQL_USER']
            passwd = app.config['MYSQL_PASSWORD']
            db = app.config['MYSQL_DB']
            connect_timeout = 5

            self.db = MySQLdb.connect(
                host=host, port=port, user=user, passwd=passwd, db=db,
                connect_timeout=connect_timeout
            )

            # Add this line to fix "Commands out of sync" error
            # self.db.autocommit(True)


def create_app():
    app = Flask(__name__)

    # mysql connection details
    app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST', 'digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
    app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT', 25060)
    app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
    app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']

    # configure mysql
    mysql.init_app(app)

    # register all blueprints
    from .views.bluep import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app

mysql = MySQL()	
app = create_app()


def connect_to_db(app):
    with app.app_context():
        mysql.init_app(app)
        # Perform your database operations


def start_app():
    app = create_app()
    thread = threading.Thread(target=connect_to_db, args=(app,))
    thread.start()
    app.run()


if __name__ == '__main__':
    start_app()
