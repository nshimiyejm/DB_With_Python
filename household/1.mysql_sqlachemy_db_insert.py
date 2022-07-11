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