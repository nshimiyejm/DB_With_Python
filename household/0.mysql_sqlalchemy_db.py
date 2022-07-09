# Connect to the Database using SQLAlchemy ORM 
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, relationship 
from sqlalchemy.ext.declarative import declarative_base 

create_engine("mysql+mysqlconnector://username:password@localhost:3306/database_name")