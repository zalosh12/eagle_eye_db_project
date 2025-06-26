import mysql.connector
from mysql.connector import Error

def create_connection(host='localhost', user='root', password='', database='eagleeyedb'):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Database connection established successfully")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        raise
