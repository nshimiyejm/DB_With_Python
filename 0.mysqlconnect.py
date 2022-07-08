import mysql.connector as mysql

def connect(db_name):
    '''
    Connection method that will allow us to access the DB
    '''
# Make sure errors get caught
    try:
        # return the connection to the DB 
        return mysql.connect(
            host='localhost',
            user='user',
            password='test',
            database = db_name
        )
    except Error as e:
        print(e)
            

if __name__ == '__main__':
    db = connect('db_name')
    
    # Get the DB cursor 
    cursor = db.cursor()
    
    # Get all the projects
    cursor.execute("SELECT * FROM db_name")
    project_records = cursor.fetchall()
    print(project_records)
    
    db.close()