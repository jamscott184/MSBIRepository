#print(df.loc[97])
#print(df.tail(5))
#df.set_index('Customer Id', inplace=True)
#print(df.index)
#print(df.loc['73B22Ac8A43DD1A'])
#print(df.to_string())
#df.sort_values('Country')
#print(pyodbc.drivers())

# Insert Customer CSV file into SQL Server
import pyodbc
import pandas as pd
import pymssql

print(pyodbc.drivers())
#SQLconn = pymssql.connect(server="PCJ", user="TestScottie", password="J5a4m3e2s1$", database="TestDb")
conn = pyodbc.connect(
    user= "TestScottie",
    password="J5a4m3e2s1$",
    Driver = ("ODBC Driver 17 for SQL Server"),
    Server = "PCJ",
    Database= "TestDb")

cursor =conn.cursor()
df = pd.read_csv("C:\temp\customers.csv")

for row in df.itertuples():
    cursor.execute('''
                 INSERT INTO TestDb.dbo.customers(Id,customerId,FirstName,LastName,Company,City,Country,Phone1,Phone2,Email,Subscription_Date,Website)
                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                 row.Id,
                 row.CustomerId,
                 row.FirstName,
                 row.LastName,
                 row.Company,
                 row.City,
                 row.Country,
                 row.Phone1,
                 row.Phone2,
                 row.Email,
                 row.SubscriptionDate,
                 row.Website
                 )

conn.commit()


#cursor.execute( " SELECT * FROM customers ORDER BY Country")
#for row in cursor:
#print(row)

df = pd.read_sql_query(" SELECT * FROM customers ORDER BY Country,Company",conn)
print(df.to_string())