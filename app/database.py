import psycopg2
con = psycopg2.connect(dbname='mtracker', user='postgres', host='localhost', password='admin')
cur = con.cursor()

cur.execute("SELECT * FROM tracker.users")
items = cur.fetchall()

con.commit()
print(items)
cur.close()
con.close()