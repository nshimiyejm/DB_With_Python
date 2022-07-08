import sqlite3

# Create a connection to the database 
connection = sqlite3.connect('movies.db')

# Create a cursor to execute statements 
cursor = connection.cursor()


# Create a tuple of data that will be added to the Database 
famousMovies = [('Pulp Fiction', 'Queen B', 1994), 
                ('Back to the Future', 'Steve Spielberg', 1985),
                ('Moonrise Kingdom', 'Wes And', 2012)
               ]

cursor.executemany('INSERT INTO Movies VALUES (?, ?, ?)', famousMovies)

# Get the Data from the DB 
records = cursor.execute("SELECT * FROM Movies")

# Get one record 
print(cursor.fetchall())

for record in records:
    print(record)

# Commit changes to the DB 
connection.commit()

# Close the connection to the DB
connection.close()