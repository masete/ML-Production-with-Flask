import MySQLdb

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
