
import mysql.connector
from mysql.connector import Error

def connect_database():
    try:
        conn = mysql.connector.connect(
            database = "LibraryManagementSystem_db",
            user = "root",
            password = "Kaa4@sql",
            host = "localhost")   
        if conn.is_connected():
            print("Connected to mySQL database successfully")
            return conn

    except Error as e:
        print(f"Error: {e}")
        return None
    
