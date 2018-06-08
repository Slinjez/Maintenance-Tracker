import psycopg2
import psycopg2.extras
from datetime import datetime as dt

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

    def createRequest(self,newrequest):
        self.connection = psycopg2.connect("dbname='maintenancetracker' user='postgres' host='localhost' password='admin'")
        self.cursor = self.connection.cursor()
        requestorid=newrequest['requestorid'],
        requesttitle= newrequest['requesttitle'],
        requestdescription= newrequest['requestdescription'],
        requesttype= newrequest['requesttype'],
        requestcreationdate= dt.now(),
        requeststatus= newrequest['requeststatus']
        # query="insert into users (requesttitle,requestdescription,requesttype,requestdate,requeststatus) values(%s,%s,%s,%s,%s);",(
        #     requesttitle,
        #     requestdescription,
        #     requesttype,
        #     requestcreationdate,
        #     requeststatus,
        #     requestorid
        # )
        #print(query)
        #self.addToDb(query)
        self.cursor.execute("INSERT INTO requests (requesttitle,requestdescription,requesttype,requestdate,requeststatus,requestorid) values(%s,%s,%s,%s,%s,%s)",(
            requesttitle,
            requestdescription,
            requesttype,
            requestcreationdate,
            requeststatus,
            requestorid))
        
        self.connection.commit()
        self.cursor.close()
        self.cursor.close()
    
    def getAllRequest(self,userid):
        query="select * from requests where requestorid='{userid}'".format(userid=userid)
        theResult=self.getFromDb(query)
        print(query)
        if not theResult:
            return None
        else:
            #print(theResult)
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

