import sqlite3

# Create a connection to the database 
connection = sqlite3.connect('movies.db')

# Create a cursor to execute statements 
cursor = connection.cursor()

# Creating filters - the comman must be after the filter value
release_year = (1994, )

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

# Commit changes to the DB 
connection.commit()

# Close the connection to the DB
connection.close()