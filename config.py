#This file contains most of the configuration variables the app needs.
#initial configuration
import uuid
import psycopg2


connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
cursor = connection.cursor()

#create tables if non exists
	

# cursor.execute("""
# SELECT EXISTS 
# (
# 	SELECT 1 
# 	FROM pg_tables
# 	WHERE tablename = 'users'
# 	AND tablename = 'requests'
# );
# """)
# connection.commit()
# tableexist= cursor.fetchall()
# print(tableexist)

cursor.execute("CREATE TABLE IF NOT EXISTS users(userid SERIAL PRIMARY KEY, username varchar(20), useremail varchar(40), password text, userrole int);")
cursor.execute("CREATE TABLE IF NOT EXISTS requests(requestid SERIAL PRIMARY KEY,requestorid int, requesttitle text, requestdescription text, requesttype int,requestdate timestamp,requeststatus int);")
connection.commit()
cursor.execute("SELECT * FROM users WHERE userrole = 1 and useremail='defadmin@maintrack.com';")
defaultuser= cursor.fetchone()

if not defaultuser:
    newuserid=str(uuid.uuid4())
    cursor.execute("INSERT INTO users(username,useremail, password,userrole) VALUES ('default','defadmin@maintrack.com', 'sha256$W2aFNlr3$2e5f12eeacb3dd06f8f5874919d7a0cb59c9b3fc1d82e15b4f102f262ca74a7f',1);")
    #connection.commit()

users=cursor.execute("SELECT useremail FROM users;")

defaultuser= cursor.fetchone()


print("db setup done")
connection.commit()
cursor.close()
cursor.close()