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
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

def create_table():
    logging.info("[POSTGRES] Creation table : start")

    #cursor.execute("DROP TABLE my_table")
    cursor.execute("CREATE TABLE IF NOT EXISTS my_table (id serial PRIMARY KEY)")
    conn.commit()

    logging.info("[POSTGRES] Creation table : end")

create_table()

# def insert_id():
#     logging.info("[POSTGRES] Insert data in table : start")

#     try:
#         insert = "INSERT INTO my_table (id) values(default)"
#         #print('value of carpet table',value)
#         cursor.execute(insert)

#         conn.commit()
#     except Exception as e:
#         logging.error('[POSTGRES] ERROOOOR !! empty list, didnt file table' +str(e))

#         logging.info("[POSTGRES] Insert data in table : end")

# insert_id()