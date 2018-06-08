#This is where the routes are defined.
# It may be split into a package of its own (app/views/) with related views grouped together into modules.
from flask import Flask, jsonify, request, make_response
import types
import time
import datetime
import pdb
import os
from app import app
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps
from app.dbFuncs import dbOperations
dbmodel = dbOperations()

defaultuserid = {"userid": ""}

users = [

]

requests = [

]

print(defaultuserid)
def tokenRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        #theRequests = [user for user in users if users["userid"] == currentUser]

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            currentUser = defaultuserid['userid']
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(currentUser, *args, **kwargs)
    return decorated


@app.route('/')
def index():
    return "will be back with the ui soon"


@app.route('/api/v2/users/signup', methods=['POST'])
def signup():
    username = request.json["username"]
    usermail = request.json["useremail"]
    userps1 = request.json["userpassword"]
    userps2 = request.json["userpassword2"]

    #lastid=uuid.uuid4()

    if not username:
        response = jsonify({"response": "please enter a username"})
        response.status_code = 400
        return response

    elif len(userps1) <= 3:
        response = jsonify(
            {"response": "Enter a password more than 4 charachters"})
        response.status_code = 400
        return response

    elif not usermail:
        response = jsonify({"response": "please enter an usermail"})
        response.status_code = 400
        return response

    elif not userps1:
        response = jsonify({"response": "please enter a password"})
        response.status_code = 400
        return response

    elif not userps2:
        response = jsonify({"response": "please confirm your password"})
        response.status_code = 400
        return response

    elif userps1 != userps2:
        response = jsonify({"response": "please enter matching passwords"})
        response.status_code = 400
        return response

    else:
        
        hashedpassword = generate_password_hash(userps1, method='sha256')

        confirmnewuser = dbmodel.confirmNewUser(usermail)
        
        if confirmnewuser == True:
            
            user = {
                #userid=str(uuid.uuid4()),
                "username": request.json["username"],
                "useremail": request.json["useremail"],
                "userpassword": hashedpassword,
                "userrole": 2
            }
            dbmodel.createUser(user)
            response = jsonify({"response": "You have succesfully registered"})
            response.status_code = 200
        else:
            response = jsonify(
                {"response": "You have already been registered"})
            response.status_code = 200
        return response


@app.route('/api/v2/users/login', methods=['POST'])
def login():
    usermail = request.json["useremail"]
    userps = request.json["userpassword"]
    hashedpassword = generate_password_hash(userps, method='sha256')
    #pdb.set_trace()
    if not usermail:
        response = jsonify({"response": "email is required"})
        response.status_code = 400
        return response

    elif len(userps) <= 3:
        response = jsonify(
            {"response": "Enter a password more than 4 charachters"})
        response.status_code = 400
        return response

    elif not userps:
        response = jsonify({"response": "password is required"})
        response.status_code = 400
        return response
    else:
        
        confirmexistingemail = dbmodel.confirmLogin(usermail)
        if not confirmexistingemail:
            response = jsonify({"response": "Unregistered email"})
            response.status_code = 400
            return response
        else:
            loginDetails =dbmodel.getLoginCredentials(usermail)
            
            correctps = loginDetails[0]['password']
            #print(correctps)
            #pdb.set_trace()
            if check_password_hash(correctps, userps) != True:
                #print("ps mismatch")
                response = jsonify({"response": "Invalid credentials"})
                response.status_code = 400
                return response
            else:
                token = jwt.encode({'publicid': loginDetails[0]['userid'], 'exp': datetime.datetime.utcnow(
                )+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY']).decode("utf-8"), 200
                #response = jsonify({"response": "logged in correctly"})
                response=jsonify({"token": token})
                response.status_code = 200
                defaultuserid['userid'] = loginDetails[0]['userid']
                #defaultuserid=theRequests[0]['userid']
                
                #print(token)
                return response


#all requests belonging to a user defaultuserid/
@app.route('/api/v2/users/requests', methods=['GET'])
@tokenRequired
def getAllRequests(currentUser):
    userid = defaultuserid['userid']
    print("user id",userid)
    if not defaultuserid['userid']:
        return jsonify({"Message": "You can not access this"})

    

    #if not request.json["userid"]:
    #userid=currentUser
    #pdb.set_trace()
    #else:
    #userid=currentUser

    
    
    theRequests=dbmodel.getAllRequest(userid)
    if not theRequests:
        response = jsonify({"requests": "No requests for this user"})
        response.status_code = 404
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response

#one request for a given user (enter from url)


@app.route('/api/v2/users/requests/<string:requestid>', methods=['GET'])
@tokenRequired
def getSingleRequest(currentUser, requestid):
    userid=defaultuserid['userid']
    if not defaultuserid['userid']:
        return jsonify({"Message": "You can not access this"})
    if not requestid or requestid == None:
        #requestid = request.json["requestid"]
        response = jsonify(
            {"response": "You have not entered an invalid request id"})
        response.status_code = 405
        requestid = 0
    try:
        if requestid is None or isinstance(int(requestid), int) == False:
            response = jsonify(
                {"requests": "You have entered an invalid request id"})
            response.status_code = 405
            return response
        else:
            requestid = int(requestid)
    except:
        response = jsonify(
            {"requests": "You have entered an request id"})
        response.status_code = 405  # Method not allowed
        return response

   
    theRequests=dbmodel.getOneRequest(userid,requestid)
    if not theRequests:
        response = jsonify({"requests": "You can not view this request"})
        response.status_code = 404
        return response
        #pdb.set_trace()
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response


#add request
@app.route('/api/v2/users/requests', methods=['POST'])
@tokenRequired
def createNewRequest(currentUser):
    #defUsr=defaultuserid
    #pdb.set_trace()
    if not defaultuserid['userid']:
        response=jsonify({"Message": "You can not access this"})
        response.status_code = 401#unauthorised
        return response
    requestorid = defaultuserid['userid']
    requesttitle = request.json["requesttitle"]
    requestdescription = request.json["requestdescription"]
    requesttype = request.json["requesttype"]
    #requestcreationdate=request.json["requestcreationdate"]
    requeststatus = 1

    #lastreuestid = requests[-1]["requestid"]
    #pdb.set_trace()
    #lastreuestid = str(uuid.uuid4())

    year = datetime.date.today().strftime("%Y")
    month = datetime.date.today().strftime("%B")
    day = datetime.date.today().strftime("%d")
    requestcreationdate = str(day)+" "+str(month)+" "+str(year)

    if not requesttitle:
        response = jsonify({"response": "Enter request title"})
        response.status_code = 206
        return response
    elif not requestdescription:
        response = jsonify({"response": "Enter request description"})
        response.status_code = 206
        return response
    elif not requesttype:
        response = jsonify({"response": "Enter request type"})
        response.status_code = 206
        return response
    else:
        newrequest = {
            
            "requestorid": requestorid,
            "requesttitle": requesttitle,
            "requestdescription": requestdescription,
            "requesttype": requesttype,
            "requestcreationdate": requestcreationdate,
            "requeststatus": 1
        }
        dbmodel.createRequest(newrequest)
        #requests.append(newrequest)
        response = jsonify(
            {"response": "Created '"+requesttitle+"' request successfully"})
        response.status_code = 200
        return response

#and finally edit a request


@app.route('/api/v2/users/requests/<string:requestid>', methods=['PUT'])
@tokenRequired
def updateRequest(currentUser, requestid):
    #pdb.set_trace()
    if not defaultuserid['userid']:
        return jsonify({"Message": "You can not access this"})
    if not requestid or requestid == None:
        requestid = 0
    try:
        if requestid is None or isinstance(int(requestid), int) == False:
            response = jsonify(
                {"requests": "You have entered an invalid request id"})
            response.status_code = 500
            return response
        else:
            requestid = int(requestid)
    except:
        response = jsonify(
            {"requests": "You have entered an invalid request id"})
        response.status_code = 500
        return response

    theRequests = [
        request for request in requests if request["requestid"] == requestid]

    if not theRequests:
        response = jsonify(
            {"respons": "Cannot edit this request because its missing"})
        response.status_code = 500
        return response
    else:
        requesttytle = request.json['requesttitle']
        reqdescription = request.json['requestdescription']

        if not requesttytle:
            response = jsonify({"response": "Enter request title"})
            response.status_code = 206
            return response

        elif not reqdescription:
            response = jsonify({"response": "Enter request description"})
            response.status_code = 206
            return response

        else:
            theRequests[0]['requesttitle'] = request.json['requesttitle']
            theRequests[0]['requestdescription'] = request.json['requestdescription']
            response = jsonify({"requests": "request edited"})
            response.status_code = 200
            return response
