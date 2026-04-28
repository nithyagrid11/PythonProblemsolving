from fastapi import Depends
import psycopg2

def get_db():
    conn = psycopg2.connect(
        dbname="moviesdb",
        user="smalladi",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    try:
        yield cursor   # gives cursor to API
    finally:
        cursor.close()
        conn.close()