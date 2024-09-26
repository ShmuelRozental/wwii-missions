import psycopg2
from psycopg2 import pool
from config import Config

db_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=Config.DB_HOST,
    database=Config.DB_NAME,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD
)

def get_db_connection():
    return db_pool.getconn()

def close_db_connection(conn):
    db_pool.putconn(conn)

def close_pool():
    db_pool.closeall()
