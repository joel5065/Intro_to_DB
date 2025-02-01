import mysql.connector


def create_database():
    try:
        mydb = mysql.connector.connect (
        host = "localhost",
        username = "root",
        password = "password1234",
        database = "alx_book_store"
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database alx_book_store is created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("Connection is closed!")

if __name__ == "__main__":
    create_database()