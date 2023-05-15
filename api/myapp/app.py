import os
from flask import Flask
import aiomysql
import MySQLdb
import asyncio



class MySQL:

	def __init__(self,app=None):
		self.db = None
		if app is not None:
			self.init_app(app)
			
	def init_app(self,app):

		async def get_db(self):
		
			if self.db is None:
				config = {
                'host': self.app.config['MYSQL_HOST'],
                'port': self.app.config['MYSQL_PORT'],
                'user': self.app.config['MYSQL_USER'],
                'password': self.app.config['MYSQL_PASSWORD'],
                'db': self.app.config['MYSQL_DB'],
                'connect_timeout': 5,
                'charset': 'utf8mb4'
            }
				self.db = await aiomysql.connect(**config)

				return self.db
			
			async def close_db(self):
				if self.db is not None:
					self.db.close()
					await self.db.wait_closed()
					self.db = None
			
			# 	host = app.config['MYSQL_HOST']
			# 	port = app.config['MYSQL_PORT']
			# 	user = app.config['MYSQL_USER']
			# 	passwd = app.config['MYSQL_PASSWORD']
			# 	db = app.config['MYSQL_DB']
			# 	connect_timeout = 5  # set timeout to 5 seconds

			# 	self.db = MySQLdb.connect(
			# 	host=host, port=port, user=user, passwd=passwd, db=db,
			# 	connect_timeout=connect_timeout
			# )
				
				# self.db = MySQLdb.connect(host=host,port=port,
				# 			  user=user,passwd=passwd,db=db
				# 			  connect_timeout=connect_timeout)
				
				# Add this line to fix "Commands out of sync" error
				# self.db.autocommit(True)
			

async def create_app(loop):
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST','digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
    app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT', 25060)
    app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
    app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']
    app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']
    app.mysql = MySQL(app=app)

    # register all blueprints
    from .views.bluep import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    @app.before_request
    async def before_request():
        app.db = await app.mysql.get_db()

    @app.teardown_request
    async def teardown_request(exception=None):
        app.db = None
        await app.mysql.close_db()

    return app

loop = asyncio.get_event_loop()
app = loop.run_until_complete(create_app(loop))

# def create_app(loop):
	
# 	app = Flask(__name__)
		
		
# 	# mysql connection details
# 	app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST','digestafrica-do-user-4558844-0.b.db.ondigitalocean.com')
# 	app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT',25060)	
# 	app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
# 	app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']	
# 	app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']
# 	# app.mysql = MySQL(app=app)
# 	# app.config['OPTIONS'] = os.environ [{
#     #         'charset': 'latin1'
#     #     }]
						 
# 	# configure mysql
# 	mysql.init_app(app)	
	
# 	# common prefix for all routes in blueprints
# 	# APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)
# 	# register all blueprints
# 	from .views.bluep import blueprints
# 	for bp in blueprints:
# 		app.register_blueprint(bp)
		
		
# 	return app


# mysql = MySQL()	
# app = create_app()	
	
