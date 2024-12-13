"""
    Author: James A. Scott
    Description: Export Customer CSV file to SQL Server Customer table.
                 The program use odbc for SQL Server access.
    Created On: 12/07/2024

"""

"""
Step 1. Import Python Libraries.

"""
import pandas as pd
import socket
import pypyodbc as odbc

"""
Step 2. Read Common Seperated Values (CSV) Comma Delimited Input file.

"""
myfile = './data/customers.csv'
df = pd.read_csv(myfile)

"""
Step 3. Input file clean up  (changes are made to the  Common Seperated Values (CSV).

"""
df.loc[5,'FirstName']='James'
df.loc[5,'LastName']='Scott'
df.to_csv(myfile)

"""
Step 4. Add Index to the Common Seperated Values (CSV).
"""

n = ['a','b']
df.index = pd.MultiIndex.from_arrays([range(len(df.index)), df.index], names= n)

"""
Step 5. Convert data frame to list object

"""

records = df.values.tolist()

"""
Step 6. Create SQL Server ODBC connection string.

"""

DRIVER = 'SQL Server Native Client 11.0'
SERVER = socket.gethostname()
DATABASE = 'TestDb'
USERNAME='TestScottie'
PASSWORD='J5a4m3e2s1$'


def connection_string(DRIVER,SERVER_NAME,DATABASE_NAME,USERNAME,PASSWORD):
    conn_string = f''''
        DRIVER = {{{DRIVER}}};
        SERVER = {SERVER};
        DATABASE = {DATABASE};
        USERNAME ={USERNAME}; 
        PASSWORD = {PASSWORD};
        Trust_Connection=no;
    '''    
    return conn_string


connection_String = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

"""
Step 7. Create Database connection object.

"""
try:
    conn=odbc.connect(connection_String)
except odbc.DatabaseError  as e:
    print('Database Error: ')
    print(str(e.value[1]))

except odbc.ODBC.Error  as e:
    print('ODBC Error: ')
    print(str(e.value[1]))    

"""
Step 8. Set the SQL Server Cursor and truncate SQL Server customer table.

"""

try:
    cursor =conn.cursor()
    cursor.execute('TRUNCATE TABLE dbo.customers')
except Exception as e:
    print(str(e.value[1]))

sql_insert = '''
 INSERT INTO [dbo].[customers]
           ([Id]
           ,[CustomerId]
           ,[FirstName]
           ,[LastName]
           ,[Company]
           ,[City]
           ,[Country]
           ,[Phone1]
           ,[Phone2]
           ,[Email]
           ,[SubscriptionDate]
           ,[Website]
           ,[CreatedOn])
     VALUES
           (?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            GETDATE())

'''


try:
     
      cursor = conn.cursor()
      cursor.executemany(sql_insert,records)
      cursor.commit();

except Exception as e:
      cursor.rollback()
      print(str(e[1]))
 
finally:
        df = pd.read_sql_query("SELECT * FROM dbo.customers ORDER BY Country,Company",conn)
        print(df.to_string())
        cursor.close()
        conn.close()










