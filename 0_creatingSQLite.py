import sqlite3

# Create a connection to the database 
connection = sqlite3.connect('movies.db')

# Create a cursor to execute statements 
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
    (Title TEXT, Director TEXT, Year INT)''')

# Commit changes to the DB 
connection.commit()

# Close the connection to the DB
connection.close()

