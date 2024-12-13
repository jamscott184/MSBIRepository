# Author: James A. Scott
# Description: Export Employee records from SQL Server to CSV file.
# Overite the exsiting employee.csv file/
# Created On: 11/29/2024

# Import Library Section

import csv
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from pathlib import Path

# Setup file path

# Connect to SQL Server

SERVER = 'PCJ'
DATABASE = 'TestDb'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME='TestScottie'
PASSWORD='J5a4m3e2s1$'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

# SQL Server Connection
engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

# Run Employee query on SQL Server
Query = pd.read_sql_query(
    '''
        SELECT  ROW_NUMBER() OVER (ORDER BY [FIRST_NAME]) AS Id
          ,[EMPLOYEE_ID]
          ,[FIRST_NAME]
          ,[LAST_NAME]
          ,[EMAIL]
          ,[PHONE_NUMBER]
          ,[HIRE_DATE]
          ,[JOB_ID]
          ,[SALARY]
          ,[COMMISSION_PCT]
          ,[MANAGER_ID]
          ,[DEPARTMENT_ID]
      FROM [dbo].[employees]
    ''',
    DATABASE_CONNECTION)

# Write SQL Server Employee records to the Employee CDV file.
DF = pd.DataFrame(Query)
DF.to_csv('employees.csv', index=False)
