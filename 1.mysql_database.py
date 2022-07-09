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

def add_new_project(cursor, project_title, project_description, task_descriptions):
    """
    Method used to insert a project to the project table
    VALUES will take a tuple to keep the data secure
    """
    project_data = (project_title, project_description)
    
    cursor.execute('''INSERT INTO projects(title, description) 
                      VALUES (%s, %s)''', project_data)
    
    # Get the last project_id that was inserted then use it when instering a task
    project_id = cursor.lastrowid
    
    tasks_data = []
    
    for description in task_descriptions:
        task_data = (project_id, description)
        tasks_data.append(task_data)
    
    cursor.executemany('''INSERT INTO tasks(project_id, description)
                   VALUES (%s, %s)''', tasks_data)
                

if __name__ == '__main__':
    db = connect('projects')
    
    # Get the DB cursor 
    cursor = db.cursor()
    
    # Create task descriptions
    tasks = ["Clean bathroom", "Clean kitchen", "Clean living Room"]
    # Call the add method 
    add_new_project(cursor, "Clean House", "Clean House by Room", tasks)
    
    db.commit()
    
    # Get all the projects
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)
    
    # Get all tasks
    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)
    
    db.close()
    
