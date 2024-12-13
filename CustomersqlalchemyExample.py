# Author: James A. Scott
# Desceiption: Export Customer CSV file to SQL Server Customer table.
# Created On: 11/29/2024

# Import library section.
import sqlalchemy
import socket
import pandas as pd
import pyodbc
import os


from sqlalchemy.engine import URL
from sqlalchemy import Engine, create_engine
from sqlalchemy.sql import text as sa_text

os.chdir(r"C:\DataFiles\CSVDataFiles\customer")

# Create SQL Server Connection
SERVER = socket.gethostname()
DATABASE = 'TestDb'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME='TestScottie'
PASSWORD='J5a4m3e2s1$'


DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine = create_engine(DATABASE_CONNECTION)
connection=engine.connect()

truncate_query = sqlalchemy.text("TRUNCATE TABLE customers")
connection.execute(truncate_query)
connection.commit()

for f1 in os.listdir():
      df=pd.read_csv(f1)
      df.to_sql("customers",con=connection, if_exists = "append", index=False)  
    
data = pd.read_sql_query("SELECT * FROM TestDb.dbo.customers ",connection)

connection.close()


       

      
   

 