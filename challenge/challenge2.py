# Todo 
# 1. Import data from a CSV file into MySQL DB 
#   - Modify the CSV if necessary 
#   - Imnport data into db named red30 
#   - Add the data into table name Sales with primary key OrderNum
#   - What is the most expensive order 
#   - Who ordered the most expensive order 
# 2. Create a table from the CSV file 
# 3. Query data from the DB  

# Add libraries 
from configparser import ConfigParser
from select import select
import pandas as pd 
from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 1. Create a connection to the DB, best practive will be reading the insformation from a config file 
configur = ConfigParser()
configur.read('config.ini')

engine = create_engine( configur.get('database', 'driver')   + "://" 
                      + configur.get('database', 'username') + ":"
                      + configur.get('database', 'password') + "@" 
                      + configur.get('database', 'host') + ":" 
                      + configur.get('database', 'port') + "/" 
                      + configur.get('database', 'db_name') , 
                      echo= True)

# 2. Set a Declarative base 
Base = declarative_base()

class Sale(Base):
    __tablename__= 'Sales'
    __table_args__={"schema":"red30"}
    
    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(250))
    cust_name = Column(String(250))
    cust_state = Column(String(250))
    prod_category = Column(String(250))
    prod_number = Column(String(250))
    prod_name = Column(String(250))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)
    
    def __repr__(self):
        return '''<Sales(order_num='{0}', order_type='{1}', 
            cust_name='{2}', cust_state='{3}', 
            prod_category='{4}', prod_number='{5}', 
            prod_name='{6}', quantity='{7}', price='{8}',
            discount='{9}',  
            order_total='{10}')>'''.format(self.order_num,
            self.order_type, self.cust_name,
            self.cust_state, self.prod_category,
            self.prod_number, self.prod_name,
            self.quantity, self.price, self.discount, self.order_total)
    
    
Base.metadata.create_all(engine)


# Read data using pandas and upload the data to the database 
file_name = "red30.csv"

# Set the dataframe 
df = pd.read_csv(file_name)

df.to_sql(con=engine, name=Sale.__tablename__, if_exists='append', index=False)

# Create a session to pull the data from the db 
session = sessionmaker()
session.configure(bind=engine)
s = session()

results = s.query(Sale.cust_name, Sale.order_total).order_by(Sale.order_total.desc()).limit(1) 


print('\n\n\n\n')
for r in results:
    print(r)

