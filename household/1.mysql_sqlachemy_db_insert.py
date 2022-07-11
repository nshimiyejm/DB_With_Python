# Connect to the Database using SQLAlchemy ORM 
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, relationship 
from sqlalchemy.ext.declarative import declarative_base 

engine = create_engine("mysql+mysqlconnector://python_user:password@localhost:3306/database_name", echo=True)

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema':'household'}
    
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))
    
    # Create a printable representation of the object (like a to string method)
    def __repr__(self):
        return "<Project(title'{0}', description='{1}'>".format(self.title, self.description)
        

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema':'household'}
    
    task_id = Column(Integer, primary_key=True)
    
    # Set a relationship between the projects and the tasks
    project_id = Column(Integer, ForeignKey('household.projects.project_id'))
    description = Column(String(length=50))
    
    project = relationship("Project")
    
    # Create a printable representation of the object (like a to string method)
    def __repr__(self):
        return "<Task(description='{0}'>".format(self.description)
        
Base.metadata.create_all(engine)

# When using models, use a session to query the database - this can be achieved by using the sessionmaker 
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# The session will allow the program to create transactions with the Database using SQLAlchemy 
# Insert a project into the projects table
organize_closet_project = Project(title='Organize closet', description='Organize closet by color and style')

# Insert the data 
session.add(organize_closet_project)
# Commit the project to prevent the task from having a null project_id 
session.commit()

tasks = [Task(project_id=organize_closet_project.project_id, description='Decide what clothes to donate'), 
         Task(project_id=organize_closet_project.project_id, description='Organize winter clothes'), 
         Task(project_id=organize_closet_project.project_id, description='Organize summer clothes')]

session.bulk_save_objects(tasks)
session.commit()


# Query documents from from the database 
our_project = session.query(Project).filter_by(title='Organize closet').first()
print(our_project)

our_tasks  = session.query(Task).all()
print(our_tasks)
