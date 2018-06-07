import psycopg2

class dbOperations():
    connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
    cursor = connection.cursor()

    def createUser(self,user):
        pass
    
    def dbmodel.confirmLogin(usermail):
        pass
    
    def getLoginCredentials(usermail):
        pass