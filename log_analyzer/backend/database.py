import mysql.connector
def connect_db():
    conn = mysql.connector.connect(
        host = 'localhost',
        user='root',
        password='nithya11',
        database='log_analyzer_db'
    )
    return conn