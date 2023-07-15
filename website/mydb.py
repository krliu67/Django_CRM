import mysql.connector

data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123456'
)
# prepare a cursor object
cursor_obj = data_base.cursor()

# create a db
cursor_obj.execute("create database elderco")

print("ALL done!")