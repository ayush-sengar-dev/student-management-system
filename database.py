import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

# print("DB_HOST:", repr(os.getenv("DB_HOST")))
# print("DB_USER:", repr(os.getenv("DB_USER")))
# print("DB_NAME:", repr(os.getenv("DB_NAME")))

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def connect_server():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )


def connect_database():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    return conn