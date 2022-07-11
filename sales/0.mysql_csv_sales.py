import mysql.connector as mysql 
import csv

connection = mysql.connect(
            host='localhost',
            user='user',
            password='test',
            database = 'db_name',
            allow_local_infile=True
        )

cursor = connection.cursor()

create_query = '''CREATE TABLE salesperson(
    id INT(255) NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(255) NOT NULL, 
    last_name VARCHAR(255) NOT NULL, 
    email_address VARCHAR(255) NOT NULL, 
    city VARCHAR(255) NOT NULL, 
    state VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id))'''

# If the table already existed, replace it with new Data
cursor.execute("DROP TABLE IF EXISTS salesperson")
cursor.execute(create_query)

# Import data from a CSV file and upload the data to the salesperson table in the sales db

# ================================================================================================
# This type of insertion will load the data as strings, this can cause a problem if the data contained in the file has any ints 

# with open('./salespeople.csv', 'r') as f:
#     # Read through each row in the file useing f
#     csv_data = csv.reader(f)
    
#     for row in csv_data:   
#         # create a tuple that can be inserted using mysql connector into the db
#         row_tuple = tuple(row)
#         cursor.execute('INSERT INTO salesperson(first_name, last_name, email_address, city, state) \
#                        VALUES ("%s", "%s","%s","%s","%s")', row_tuple)
# ================================================================================================    
q = '''LOAD DATA LOCAL INFILE 
    '/Users/administrator_1/Documents/Repos/Python-DB/DB_With_Python/sales/salespeople.csv'
    INTO TABLE salesperson 
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"' 
    (first_name, last_name, email_address, city, state);'''
cursor.execute(q)

connection.commit()

cursor.execute("SELECT * FROM salesperson LIMIT 10")
print(cursor.fetchall())

connection.close()