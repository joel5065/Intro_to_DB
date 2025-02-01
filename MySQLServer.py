import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    username = "root",
    password = "password1234",
    database = "alx_book_store"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database alx_book_store is created successfully!")


mycursor.close()
mydb.close()