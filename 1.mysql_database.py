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
            user='python_user',
            password='TestL3arn!#$!',
            database = db_name
        )
    except Error as e:
        print(e)
            

if __name__ == '__main__':
    db = connect('projects')
    
    # Get the DB cursor 
    cursor = db.cursor()
    
    # Get all the projects
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)
    
    
    db.close()
    
