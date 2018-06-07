import psycopg2
import psycopg2.extras

class dbOperations():
    connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
    cursor = connection.cursor()

    def confirmNewUser(self,usermail):        
        query="select * from users where useremail='{usermail}'".format(usermail=usermail)
        theResult=self.getFromDb(query)
        if not theResult:
            return True
        else:
            return False

    def createUser(self,user):
        username=user['username']
        useremail=user['useremail']
        userpassword=user['userpassword']
        userrole=user['userrole']
        query="insert into users (username,useremail,password,userrole) values('{username}','{useremail}','{userpassword}','{userrole}')".format(
            username=username,
            useremail=useremail,
            userpassword=userpassword,
            userrole=userrole
        )
        self.addToDb(query)
        
    
    def confirmLogin(self,usermail):
        query="select * from users where useremail='{usermail}'".format(usermail=usermail)
        theResult=self.getFromDb(query)
        if not theResult:
            return False
        else:
            return True
    
    def getLoginCredentials(self,usermail):
        query="select * from users where useremail='{usermail}'".format(usermail=usermail)
        theResult=self.getFromDb(query)
        if not theResult:
            return None
        else:
            return theResult

    def getFromDb(self,query):
        self.connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
        cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute (query)
        resultset =cur.fetchall()
        dict_result = []
        for row in resultset:
            dict_result.append(dict(row))
        return dict_result
        self.connection.commit()
        self.cursor.close()
        self.cursor.close()

    def addToDb(self,query):
        self.connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.connection.commit()
        self.cursor.close()
        self.cursor.close()

