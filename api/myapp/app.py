import os
from flask import Flask
import asyncio
# import aiohttp
import aiomysql
import MySQLdb


class MySQL:
    def __init__(self, app=None):
        self.db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        async def get_db():
            if self.db is None:
                config = {
                    'host': app.config['MYSQL_HOST'],
                    'port': app.config['MYSQL_PORT'],
                    'user': app.config['MYSQL_USER'],
                    'password': app.config['MYSQL_PASSWORD'],
                    'db': app.config['MYSQL_DB'],
                    'connect_timeout': 5,
                    'charset': 'utf8mb4'
                }
                self.db = await aiomysql.connect(**config)
            return self.db

        async def close_db():
            if self.db is not None:
                self.db.close()
                await self.db.wait_closed()
                self.db = None

        app.get_db = get_db
        app.close_db = close_db


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


# async def get_inv_analysis():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://localhost:5000/api/v1/dealsByYear_linePlot/') as response:
#             data = await response.json()
#             return data


mysql = MySQL()
app = create_app()

loop = asyncio.get_event_loop()
# data = loop.run_until_complete(get_inv_analysis())
# print(data)
