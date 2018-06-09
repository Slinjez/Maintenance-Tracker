class Request:

    def __init__(self, requestid, requesttitle, requestdescription, requesttype, requestdate, requeststatus):
        self.requestid = requestid
        self.requesttitle = requesttitle
        self.requestdescription = requestdescription
        self.requesttype = requesttype
        self.requestdate = requestdate
        self.requeststatus = requeststatus

    def setRequestd(self, requestid):
        self.requestid

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
