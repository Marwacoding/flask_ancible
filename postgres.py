import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
import logging

#print(os.environ["pw"])
logging.basicConfig(filename = "postgress-ancible.log", 
                    level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

host = os.environ["host"]
dbname = "my_db"
user = os.environ["user"]
password = os.environ["password"]
sslmode = "require" 

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
#print(conn_string)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

def create_table():
    logging.info("[POSTGRES] Creation table : start")

    #cursor.execute("DROP TABLE my_table")
    cursor.execute("CREATE TABLE IF NOT EXISTS my_table (id serial PRIMARY KEY)")
    print("key")
    conn.commit()

    logging.info("[POSTGRES] Creation table : end")

create_table()