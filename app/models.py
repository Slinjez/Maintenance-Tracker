#This is where you define the models of the application. 
# This may be split into several modules in the same way as views.py.

import psycopg2

con = psycopg2.connect('dbname='testdb' user='postgres' host='localhost' password='admin')
cur = con.cursor()
cur.execute("CREATE TABLE test(id serial PRIMARY KEY, name varchar, email varchar)")

cur.close()
con.close()
