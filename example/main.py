import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=host.docker.internal;"
                      "Database=master;"
                      "uid=sa;"
                      "pwd=Passw@rd;")

cursor = conn.cursor()
cursor.execute("SELECT 'It works!'")

for row in cursor:
    print(row[0])