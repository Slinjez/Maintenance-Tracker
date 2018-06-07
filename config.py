#This file contains most of the configuration variables the app needs.
#initial configuration
import uuid
import psycopg2


connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
cursor = connection.cursor()

#create tables
cursor.execute("CREATE TABLE users(userid text PRIMARY KEY, username varchar(20), useremail varchar(40), password text, userrole int);")
cursor.execute("CREATE TABLE requests(requestid serial PRIMARY KEY, requesttitle text, requestdescription text, requesttype int,requestdate timestamp,requeststatus int);")

cursor.execute("SELECT * FROM users WHERE userrole = 1 and useremail='defadmin@maintrack.com';")
defaultuser= cursor.fetchone()

if not defaultuser:
    newuserid=str(uuid.uuid4())
    cursor.execute("INSERT INTO users(userid,username,useremail, password,userrole) VALUES ('newuserid','default','defadmin@maintrack.com', 'admin',1);")

users=cursor.execute("SELECT useremail FROM users;")
defaultuser= cursor.fetchone()

print("db setup done")

cursor.close()
cursor.close()