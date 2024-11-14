import psycopg2
from psycopg2 import sql

def connect_db():
    conn = psycopg2.connect(
        host = '172.27.80.1',
        database = 'LLM',
        user = 'postgres',
        password = '1201'
    )
    
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    create_table_query = """
                        CREATE TABLE IF NOT EXISTS complaint_db (
                        id SERIAL PRIMARY KEY,
                        orginal_text TEXT NOT NULL,
                        summary TEXT,
                        keywords TEXT)
                        """
                        
    cursor.execute(create_table_query)
    conn.commit()
    
    cursor.close()
    conn.close()