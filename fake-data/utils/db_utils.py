import asyncio

import aiomysql
import pymysql

"""
This is a simple script to generate fake data for testing.
"""


def create_db_connection(host_name, user_name, user_password, db_name):
    """Create a database connection."""
    config = {
        "host": host_name,
        "user": user_name,
        "password": user_password,
        "database": db_name,
    }
    connection = pymysql.connect(host=host_name, user=user_name, password=user_password, database=db_name)
    print("MySQL Database connection successful")
    return connection


async def create_pool(loop, host_name, user_name, user_password, db_name):
    pool = await aiomysql.create_pool(
        host=host_name,
        port=3306,
        user=user_name,
        password=user_password,
        db=db_name,
        charset='utf8mb4',
        autocommit=True,
        loop=loop
    )
    # this pool will be an async pool
    # pool.close() is called async
    # pool.close()
    return pool


async def insert_data(pool, sql):
    # print(sql)
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            # sql = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
            # values = ("value1", "value2")  # 根据实际情况替换这里的值
            await cursor.execute(sql)
            print(f"Inserted {cursor.rowcount} row(s)")


async def select_data(pool, sql):
    # print(sql)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            # sql = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
            # values = ("value1", "value2")  # 根据实际情况替换这里的值
            # print("again")
            await cur.execute(sql)
            print(cur.description)
            # cur.fetchone()
            print(f"selected {cur.rowcount} row(s)")


def run_async_task_in_loop(task_func, loop=None):
    """
    Runs an asyncio task within an event loop and blocks until the task is complete.
    :param task_func: An async function to run.
    :param loop: Optional, an existing event loop to use. If not provided, a new one will be created.
    """
    if loop is None:
        loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(task_func())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        loop.close()
