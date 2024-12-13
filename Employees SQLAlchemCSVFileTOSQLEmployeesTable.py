

"""
  Author: James A. Scott
  Description: Export Employee CSV file to SQL Alchemy SQL Server Employees table.
  Created On: 11/29/2024
"""

"""
# Step 1. Import Python Libraries section:
"""
import sqlalchemy
import socket
import pandas as pd

from sqlalchemy.engine import URL
from sqlalchemy import Engine, create_engine

"""
# Step 2. Create SQL Server connection section:
"""
SERVER = socket.gethostname()
DATABASE = 'TestDb'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME='TestScottie'
PASSWORD='J5a4m3e2s1$'

DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine = create_engine(DATABASE_CONNECTION)
connection=engine.connect()

truncate_query = sqlalchemy.text("TRUNCATE TABLE dbo.employees")
connection.execute(truncate_query)
connection.commit()

"""
# Step 3. Read Employees CSV file section:
"""
myfile = './data/employees.csv'
df = pd.read_csv(myfile)
df.to_sql("employees",con=connection, if_exists = "append", index=False)  

"""
# Step 4. close connection section:
"""
connection.close()