import psycopg2

con = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Kaliakakya", 
  host="127.0.0.1", 
  port="5432"
)

print("Database opened successfully")
cur = con.cursor()  
cur.execute('''CREATE TABLE USERS  
     (USER_ID INT PRIMARY KEY NOT NULL,
     USERNAME TEXT NOT NULL,
     PASSWORD CHAR(50) NOT NULL,
     DEPARTMENT CHAR(50));''')

print("Table created successfully")
con.commit()  
con.close()