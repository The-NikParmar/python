import mysql.connector

def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydata")

conn()
