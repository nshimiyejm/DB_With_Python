import sqlite3

# Create a connection to the database 
connection = sqlite3.connect('movies.db')

# Create a cursor to execute statements 
cursor = connection.cursor()

# Insert data into the Movies table
cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Jean-Marie', 1978 ) ")

# Get the Data from the DB 
cursor.execute("SELECT * FROM Movies")

# Get one record 
print(cursor.fetchone())


# Commit changes to the DB 
connection.commit()

# Close the connection to the DB
connection.close()