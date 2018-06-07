#This is where you define the models of the application. 
# This may be split into several modules in the same way as views.py.
import uuid

class user():
    def __init__(self):
        self.users = {}
        self.usertoken = {}

    def addUser(self,userid,username,useremail,userpassword,userrole):
        self.userid=userid
        self.username=username
        self.useremail=useremail
        self.userpassword=userpassword
        self.userrole=userrole

class requests():

    def addRequests(self,requestid,requestorid,requesttitle,requestdescription,requesttype,requestdate,requeststatus):
        self.requestid=requestid
        self.requestorid=requestorid
        self.requesttitle=requesttitle
        self.requestdescription=requestdescription
        self.requesttype=requesttype
        self.requestdate=requestdate
        self.requeststatus=requeststatus
    


