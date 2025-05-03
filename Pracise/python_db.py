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

# Read
con.execute('SELECT top 5 * FROM Emp')
result = con.fetchall()
for r in result:
    print(r)

# Update 
con.execute("Update emp set first_name = 'Mahi' where employee_id = 198")
con.execute('SELECT * FROM Emp where employee_id = 198')
print(con.fetchall())

# Insert
insert_query = "Insert into emp(first_name, last_name) values(?,?)"
con.execute(insert_query,('niku1','kolhe1'))
con.execute("SELECT * FROM Emp where first_name = 'niku1'")
print(con.fetchall())


# delete
delete_qury = "delete from emp where first_name = 'niku1'"
con.execute(delete_qury)
con.execute("SELECT * FROM Emp where first_name = 'niku'")
print(con.fetchall())


