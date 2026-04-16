import psycopg2

conn = psycopg2.connect(
    dbname="moviesdb",
    user="smalladi",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()