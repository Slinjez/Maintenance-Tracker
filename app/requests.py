class Requests(object):

    def __init__(self,requestorid, requestid, requesttitle, requestdescription, requesttype, requestdate, requeststatus):
        self.requestid = requestid
        self.requesttitle = requesttitle
        self.requestdescription = requestdescription
        self.requesttype = requesttype
        self.requestdate = requestdate
        self.requeststatus = requeststatus
        self.requestorid=requestorid

    def setRequestd(self, requestid):
        self.requestid

    def setRequestoId(self,requestorid):
        self.requestorid=requestorid

    def setRequestTitle(self, requesttitle):
        self.requesttitle

    def setRequestDescription(self, requestdescription):
        self.requestdescription

    def setRequestType(self, requesttype):
        self.requesttype

    def setRequestDate(self, requestdate):
        self.requestdate

    def setRequestStatus(self, requeststatus):
        self.requeststatus

    def getRequestd(self):
        return self.requestid

    def getRequestorId(self):
        return self.requestorid

    def getRequestTitle(self):
        return self.requesttitle

    def getRequestDescription(self):
        return self.requestdescription

    def getRequestType(self):
        return self.requesttype

    def getRequestDate(self):
        return self.requestdate

    def getRequestStatus(self):
        return self.requeststatus

    def setRequest(self,requestorid,requesttitle,requestdescription,requesttype,requestdate,requeststatus):
        self.requestorid=requestorid
        self.requesttitle=requesttitle
        self.requestdescription=requestdescription
        self.requesttype=requesttype
        self.requestdate=requestdate
        self.requeststatus=requeststatus
    
    def addRequest(self,requestid,requestorid,requesttitle,requestdescription,requesttype,requestdate,requeststatus):
        self.requestid=requestid
        self.requestorid=requestorid
        self.requesttitle=requesttitle
        self.requestdescription=requestdescription
        self.requesttype=requesttype
        self.requestdate=requestdate
        self.requeststatus=requeststatus
    
    def getRequest(self):
        return Requests

