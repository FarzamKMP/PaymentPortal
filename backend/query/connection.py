import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DATABASEHOST"),
            user=os.getenv("DATABASEUSER"),
            password=os.getenv("DATABASEPASSWORD"),
            database=os.getenv("DATABASENAME")
        )
        print("Connection to MySQL DB successful")
        return connection
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
        return None