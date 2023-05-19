# import asyncio
# import aiomysql
from . import app

async def get_db_connection():
    return await app.get_db()

