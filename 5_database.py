from importlib.metadata import metadata
from sqlite3 import connect
import sqlalchemy as db

# The engine variable allows you to have muliple database connections and manages the connections 

engine = db.create_engine('sqlite:///movies.db')

connection = engine.connect()

metadata = db.MetaData()
# Metadata contains the information about the db table 
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# Select all records 
query = db.select([movies])

result_proxy = connection.execute(query)

# use the result_proxy to retrieve the data 
result_set = result_proxy.fetchall()

print(result_set[0])
print(result_set[:2])

# Filtering 
query = db.select([movies]).where(movies.columns.Director == "Queen B")


result_proxy = connection.execute(query)
# use the result_proxy to retrieve the data 
result_set = result_proxy.fetchall()
print(result_set[0])


# Inserting new value in the database - create a query that will be executed to add the values 
query = movies.insert().values(Title="Fast 4", Director="Paul M", Year="2015")
connection.execute(query) 
