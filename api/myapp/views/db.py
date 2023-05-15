# import asyncio
# import aiomysql
from myapp import app

async def get_db_connection():
    return await app.get_db()

