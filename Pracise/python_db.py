import pyodbc

# SQL Server Connections
server = 'localhost'
db = 'Practise_db'
user = 'SA'
password = 'Mahikolhe@23'
driver = 'ODBC Driver 18 for SQL Server'

try:
    conn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={db};UID={user};PWD={password};TrustServerCertificate=yes;")
    print('Connection succesfull')
except Exception as e:
    print('connect failed')

con = conn.cursor()

con.execute('SELECT * FROM Emp')

result = con.fetchall()




