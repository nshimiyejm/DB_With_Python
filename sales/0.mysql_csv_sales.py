import mysql.connector as mysql 
import csv

connection = mysql.connect(
            host='localhost',
            user='user',
            password='test',
            database = 'db_name'
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
with open('./salesperson.csv', 'r') as f:
    # Read through each row in the file useing f
    csv_data = csv.reader(f)
    
    for row in csv_data:
        row_tuple = tuple(row)
        cursor.execute()
    
    
    


