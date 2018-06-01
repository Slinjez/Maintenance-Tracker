
from app import app
from flask import jsonify, request, session
import types
import time
import datetime
import pdb



defaultuserid = 2


#some inits
users = [
    {
        'userid': 1,
        'username': 'daisy',
        'useremail': 'daisy@daisy.com',
        'userpassword': 'herps'
    },
    {
        'userid': 2,
        'username': 'thiga',
        'useremail': 'mwangiwathiga@gmail.com',
        'userpassword': 'myps'
    }
]

requests = [
    {
        'requestid': 1,
        'requestorid': 1,
        'requesttitle': 'An Awesome Title',
        'requestdescription': 'This is my request description',
        "requesttype": 1,
        'requestcreationdate': '30 may 2018',
        'requeststatus': 1
    },
    {
        'requestid': 2,
        'requestorid': 2,
        'requesttitle': 'Test hack',
        'requestdescription': 'This is my request description',
        'requesttype': 2,
        'requestcreationdate': '30 may 2018',
        'requeststatus': 1
    },
    {
        'requestid': 3,
        'requestorid': 2,
        'requesttitle': 'A Better Title',
        'requestdescription': 'This is my request description',
        'requesttype': 1,
        'requestcreationdate': '30 may 2018',
        'requeststatus': 1
    }
]


@app.route('/')
def index():
    return "will be back with the ui soon"


@app.route('/api/v1/users/signup', methods=['POST'])
def signup():
    username = request.json["username"]
    usermail = request.json["useremail"]
    userps1 = request.json["userpassword1"]
    userps2 = request.json["userpassword2"]

    lastid = users[-1]["userid"]
    #pdb.set_trace()
    lastid += 1

    if not username:
        response = jsonify({"response": "please enter a username"})
        response.status_code = 200
        return response

    elif not usermail:
        response = jsonify({"response": "please enter an usermail"})
        response.status_code = 200
        return response

    elif not userps1:
        response = jsonify({"response": "please enter a password"})
        response.status_code = 200
        return response

    elif not userps2:
        response = jsonify({"response": "please confirm your password"})
        response.status_code = 200
        return response

    elif userps1 != userps2:
        response = jsonify({"response": "please enter matching passwords"})
        response.status_code = 200
        return response

    else:
        #pdb.set_trace()
        newsignuprequest = {
            "userid": lastid,
            "username": request.json["username"],
            "useremail": request.json["useremail"],
            "userpassword1": request.json["userpassword1"]
        }
        #check if new user
        theRequests = [
            theuser for theuser in users if theuser["useremail"] == usermail]
        if not theRequests:
            users.append(newsignuprequest)
            response = jsonify({"response": "You have succesfully registered"})
            response.status_code = 200
        else:
            response = jsonify(
                {"response": "You have already been registered"})
            response.status_code = 200
        return response


@app.route('/api/v1/users/login', methods=['POST'])
def login():

    usermail = request.json["useremail"]
    userps = request.json["userpassword"]
    #pdb.set_trace()
    if not usermail:
        response = jsonify({"response": "email is required"})
        response.status_code = 200
        return response

    elif not userps:
        response = jsonify({"response": "password is required"})
        response.status_code = 200
        return response
    else:
        theRequests = [
            theuser for theuser in users if theuser["useremail"] == usermail]

        if not theRequests:
            response = jsonify({"response": "Unregistered email"})
            response.status_code = 200
            return response
        else:
            correctps = theRequests[0]['userpassword']
            userid = theRequests[0]['userid']
            #pdb.set_trace()
            if correctps != userps:
                response = jsonify({"response": "Invalid credentials"})
                response.status_code = 200
                return response
            else:
                
                defaultuserid = userid
                response = jsonify({"response": "user "+defaultuserid+" logged in correctly"})
                response.status_code = 200
                #pdb.set_trace()
                return response


#all requests belonging to a user defaultuserid
@app.route('/api/v1/users/requests', methods=['GET'])
def getAllRequests():
    userid = defaultuserid
    #pdb.set_trace()
    if not userid or userid == None:
        userid = 0
    try:
        if userid is None or isinstance(int(userid), int) == False:
            response = jsonify(
                {"requests": "You have entered an invalid user id"})
            response.status_code = 200
            return response
        else:
            userid = int(userid)
    except:
        response = jsonify({"requests": "You have entered an invalid user id"})
        response.status_code = 405  # Method not allowed
        return response

    theRequests = [
        request for request in requests if request["requestorid"] == userid]

    if not theRequests:
        response = jsonify({"requests": "No requests for this user"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"all requests for user "+str(userid): theRequests})
        response.status_code = 200
        return response

#one request for a given user (enter from url)


@app.route('/api/v1/users/requests/<string:requestid>', methods=['GET'])
def getSingleRequest(requestid):
    if not requestid or requestid == None:
        requestid = 0
    try:
        if requestid is None or isinstance(int(requestid), int) == False:
            response = jsonify(
                {"response": "You have entered an invalid requesting id"})
            response.status_code = 404
            return response
        else:
            requestid = int(requestid)
    except:
        response = jsonify(
            {"response": "You have entered an invalid request id"})
        response.status_code = 405  # Method not allowed
        return response

    theRequests = [
        request for request in requests if request["requestid"] == requestid]

    if not theRequests:
        response = jsonify({"response": "This request does not exist"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"specific response": theRequests})
        response.status_code = 200
        return response

#add request


@app.route('/api/v1/users/requests', methods=['POST'])
def createNewRequest(defUsr=defaultuserid):
    #requestid=request.json["requestid"]
    #requestorid=request.json["requestorid"]
    requestorid = defaultuserid
    requesttitle = request.json["requesttitle"]
    requestdescription = request.json["requestdescription"]
    requesttype = request.json["requesttype"]
    #requestcreationdate=request.json["requestcreationdate"]
    requeststatus = 1

    lastreuestid = requests[-1]["requestid"]
    #pdb.set_trace()
    lastreuestid += 1

    year = datetime.date.today().strftime("%Y")
    month = datetime.date.today().strftime("%B")
    day = datetime.date.today().strftime("%d")
    requestcreationdate = str(day)+" "+str(month)+" "+str(year)

    if not requesttitle:
        return jsonify({"response": "Enter request title"})
    elif not requestdescription:
        return jsonify({"response": "Enter request description"})
    elif not requesttype:
        return jsonify({"response": "Select request type"})
    else:
        newrequest = {
            "requestid": lastreuestid,
            "requestorid": requestorid,
            "requesttitle": requesttitle,
            "requestdescription": requestdescription,
            "requesttype": requesttype,
            "requestcreationdate": requestcreationdate,
            "requeststatus": requeststatus
        }

        requests.append(newrequest)
        return jsonify({"response": "Created '"+requesttitle+"' request successfully"})

#and finally edit a request


@app.route('/api/v1/users/requests/<string:requestid>', methods=['PUT'])
def updateRequest(requestid):
    if not requestid or requestid == None:
        requestid = 0
    try:
        if requestid is None or isinstance(int(requestid), int) == False:
            response = jsonify(
                {"requests": "You have entered an invalid request id"})
            response.status_code = 200
            return response
        else:
            requestid = int(requestid)
    except:
        response = jsonify(
            {"requests": "You have entered an invalid request id"})
        response.status_code = 405  # Method not allowed
        return response

    theRequests = [
        request for request in requests if request["requestid"] == requestid]

    if not theRequests:
        response = jsonify({"response": "Cannot edit this request"})
        response.status_code = 200
        return response
    else:
        thenewtitle = request.json['requesttitle']
        thenewdescription = request.json['requestdescription']
        thenewrequestrequesttype = request.json['requesttype']
        if not thenewtitle:
            response = jsonify({"response": "Enter new title"})
            response.status_code = 200
            return response
        elif not thenewdescription:
            response = jsonify({"response": "Enter new description"})
            response.status_code = 200
            return response
        elif not thenewrequestrequesttype:
            response = jsonify({"response": "Enter new request type"})
            response.status_code = 200
            return response
        elif isinstance(thenewrequestrequesttype, int) == False:
            response = jsonify({"response": "Enter integer as request type"})
            response.status_code = 200
            return response
        else:
            theRequests[0]['requesttitle'] = request.json['requesttitle']
            theRequests[0]['requestdescription'] = request.json['requestdescription']
            response = jsonify({"response": "request edited"})
            response.status_code = 200
            return response


