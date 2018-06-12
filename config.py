#This file contains most of the configuration variables the app needs.
#initial configuration
import uuid
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash


connection = psycopg2.connect("dbname='d7ald91h9iu1kq' user='fhxfwhyrjjqvwc' host='postgres://fhxfwhyrjjqvwc:a566f768bde497878d4487b3f7d6fbdf4e881ebf8df2efa5402a0a1009ecbb7c@ec2-54-243-137-182.compute-1.amazonaws.com:5432/d7ald91h9iu1kq
' password='a566f768bde497878d4487b3f7d6fbdf4e881ebf8df2efa5402a0a1009ecbb7c'")
cursor = connection.cursor()


hashedpassword = generate_password_hash('admin', method='sha256')
cursor.execute("CREATE TABLE IF NOT EXISTS users(userid SERIAL PRIMARY KEY, username varchar(20), useremail varchar(40), password text, userrole int);")
cursor.execute("CREATE TABLE IF NOT EXISTS requests(requestid SERIAL PRIMARY KEY,requestorid int, requesttitle text, requestdescription text, requesttype int,requestdate timestamp,requeststatus int);")
connection.commit()
cursor.execute("SELECT * FROM users WHERE userrole = 1 and useremail='defadmin@maintrack.com';")
defaultuser= cursor.fetchone()

if not defaultuser:
    newuserid=str(uuid.uuid4())
    cursor.execute("INSERT INTO users(username,useremail, password,userrole) VALUES ('default','defadmin@maintrack.com', '{ps}',1);".format(ps=hashedpassword))
    connection.commit()

users=cursor.execute("SELECT useremail FROM users;")

defaultuser= cursor.fetchone()


print("db setup done")
connection.commit()
cursor.close()
