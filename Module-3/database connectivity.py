import pymysql


mydb = pymysql.connect(host="localhost",user="",password="root")

mycursor =mydb.cursor()

# create database 
mycursor.execute("create database if not exists topspython")

# create table
mydb = pymysql.connect(host="localhost",user="",password="root",database="topspython")

mycursor = mydb.cursor()

mycursor.execute("create table if not exists student (id int primary key auto_increment , name varchar(20), subject varchar(20))")

mydb.commit()
