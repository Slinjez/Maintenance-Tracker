class User:

    def __init__(self, userid, username, useremail, userpassword, userrole):
        self.userid = userid
        self.username = username
        self.useremail = useremail
        self.userpassword = userpassword
        self.userrole = userrole

    def setUserId(self, userid):
        self.userid = userid

    def setUserName(self, username):
        self.username = username

    def setUserEmail(self, useremail):
        self.useremail = useremail

    def setUserpassword(self, userpassword):
        self.userpassword = userpassword

    def setUserRole(self, userrole):
        self.userrole = userrole

    def getUserId(self):
        return self.userid

    def getUserName(self):
        return self.username

    def getUserEmail(self):
        return self.useremail

    def getUserpassword(self):
        return self.userpassword

    def getUserRole(self):
        return self.userrole
