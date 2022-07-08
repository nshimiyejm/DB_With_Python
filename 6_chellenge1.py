# Create a Users' table 
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData

# create a connection to the database 
engine = db.create_engine('sqlite:///movies.db')
conn = engine.connect()
meta = MetaData()


# Create a table called users that has the following information
users = Table(
    'Users', meta, 
    Column('user_id', Integer, primary_key = True), 
    Column('first_name', String),
    Column('last_name', String), 
    Column('email', String),
    )

meta.create_all(engine)

# Instering values in the Database 
insert_query = users.insert().values([
            {"first_name":'Johnny1',"last_name": 'Quest1', "email": "quest1@sqlalchemy.org"},
            {"first_name":'Johnny2',"last_name": 'Quest2', "email": "quest2@sqlalchemy.org"},
            {"first_name":'Johnny3',"last_name": 'Quest3', "email": "quest3@sqlalchemy.org"},
            {"first_name":'Johnny4',"last_name": 'Quest4', "email": "quest4@sqlalchemy.org"},
            {"first_name":'Johnny5',"last_name": 'Quest5', "email": "quest5@sqlalchemy.org"},
        ])

conn.execute(insert_query)

# Selecting all the emails from the DB 
query = db.select([users.columns["email"]])
result_proxy = conn.execute(query)
result_set = result_proxy.fetchall()

print(result_set)

# Delete all the records from the table 
# result = users.delete()
# conn.execute(result)