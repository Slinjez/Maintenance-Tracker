import psycopg2

def migrate(app):
    connect = psycopg2.connect("dbname='{}' user='postgres' host='localhost' password='admin'")
    curr=connect.cursor()
    

    checkadmin=curr.fetchone()

