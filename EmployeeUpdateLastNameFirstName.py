# Author: James Scott 
# Description: Update Employee Last Name First Name.
# Created On: 11/29/2024

import sqlalchemy
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# SQL Server Connection Credentials

SERVER = 'PCJ'
DATABASE = 'TestDb'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME='TestScottie'
PASSWORD='J5a4m3e2s1$'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

# SQL Server Connection
engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

# 
data = pd.read_sql_query("SELECT TOP 1 * FROM [TestDb].[dbo].[employees] WHERE  [Index] = 139 ORDER BY [Index] desc", connection)
data.iloc[0,2]="James"
data.iloc[0,3]="Scott"
print(data)