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
from app.requests import Requests
from app.user import User
thisUser = User('', '', '', '', '')
thisRequest = Requests('', '', '', '', '', '', '')
from app.dbFuncs import dbOperations
dbmodel = dbOperations()


defaultuserid = {"userid": ""}
userrole = {"role": ""}

users = [

]

requests = [

]


def tokenRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message": "Token is missing"}), 401

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

            newUser = thisUser.createUser(
                username, usermail, hashedpassword, 2)
            dbmodel.saveUser(newUser)
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
        LoginUser = thisUser.createUserEmailOnly(usermail)
        confirmexistingemail = dbmodel.confirmLogin(LoginUser)
        if not confirmexistingemail:
            response = jsonify({"response": "Unregistered email"})
            response.status_code = 400
            return response
        else:
            loginDetails = dbmodel.getLoginCredentials(LoginUser)

            correctps = loginDetails[0]['password']
            therole = loginDetails[0]['userrole']

            if check_password_hash(correctps, userps) != True:

                response = jsonify({"response": "Invalid credentials"})
                response.status_code = 400
                return response
            else:
                token = jwt.encode({'publicid': loginDetails[0]['userid'], 'therole': therole, 'exp': datetime.datetime.utcnow(
                )+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY']).decode("utf-8"), 200

                response = jsonify({"token": token})
                response.status_code = 200
                defaultuserid['userid'] = loginDetails[0]['userid']
                userrole['role'] = therole

                return response


@app.route('/api/v2/login', methods=['POST'])
def adminLogin():
    usermail = request.json["useremail"]
    userps = request.json["userpassword"]

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
        LoginUser = thisUser.createUserEmailOnly(usermail)
        confirmexistingemail = dbmodel.confirmLogin(LoginUser)
        if not confirmexistingemail:
            response = jsonify({"response": "Unregistered email"})
            response.status_code = 400
            return response
        else:
            loginDetails = dbmodel.getLoginCredentials(LoginUser)

            correctps = loginDetails[0]['password']
            therole = loginDetails[0]['userrole']

            if check_password_hash(correctps, userps) != True:
                response = jsonify({"response": "Invalid credentials"})
                response.status_code = 400
                return response
            else:
                token = jwt.encode({'publicid': loginDetails[0]['userid'], 'therole': therole, 'exp': datetime.datetime.utcnow(
                )+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY']).decode("utf-8"), 200

                response = jsonify({"token": token})
                response.status_code = 200
                defaultuserid['userid'] = loginDetails[0]['userid']
                userrole['role'] = therole

                return response


#all requests belonging to a user defaultuserid/
@app.route('/api/v2/users/requests', methods=['GET'])
@tokenRequired
def getAllRequests(currentUser):
    userid = defaultuserid['userid']

    if not defaultuserid['userid']:
        return jsonify({"Message": "You can not access this"})

    theRequests = dbmodel.getAllRequest(userid)

    if not theRequests:
        response = jsonify({"requests": "No requests for this user"})
        response.status_code = 404
        return response
    else:
        for request in theRequests:
            thisRequest.addRequest(request['requestid'], request['requestorid'], request['requesttitle'],
                                   request['requestdescription'], request['requesttype'], request['requestdate'], request['requeststatus'])

        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response


@app.route('/api/v2/users/requests/<string:requestid>', methods=['GET'])
@tokenRequired
def getSingleRequest(currentUser, requestid):
    userid = defaultuserid['userid']
    if not defaultuserid['userid']:
        return jsonify({"Message": "You can not access this"})
    if not requestid or requestid == None:

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

    theRequests = dbmodel.getOneRequest(userid, requestid)
    if not theRequests:
        response = jsonify({"requests": "You can not view this request"})
        response.status_code = 404
        return response

    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response


#add request
@app.route('/api/v2/users/requests', methods=['POST'])
@tokenRequired
def createNewRequest(currentUser):

    if not defaultuserid['userid']:
        response = jsonify({"Message": "You can not access this"})
        response.status_code = 401  # unauthorised
        return response
    requestorid = defaultuserid['userid']
    requesttitle = request.json["requesttitle"]
    requestdescription = request.json["requestdescription"]
    requesttype = request.json["requesttype"]

    requeststatus = 1

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
        #print("main user id"+str(requestorid))
        thisRequest.setRequest(requestorid,requesttitle,requestdescription,requesttype,requestcreationdate,requeststatus)
        dbmodel.createRequest(thisRequest)

        response = jsonify(
            {"response": "Created '"+requesttitle+"' request successfully"})
        response.status_code = 200
        return response


@app.route('/api/v2/users/requests/<string:requestid>', methods=['PUT'])
@tokenRequired
def updateRequest(currentUser, requestid):

    if not defaultuserid['userid']:
        return jsonify({"Message": "You can not access this"})
    userid = defaultuserid['userid']
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

    theRequests = dbmodel.getOneRequest(userid, requestid)
    if not theRequests:
        response = jsonify(
            {"respons": "Cannot edit this request because it's not yours'"})
        response.status_code = 500
        return response
    else:
        requesttytle = request.json['requesttitle']
        reqdescription = request.json['requestdescription']
        requesttype = request.json['requesttype']

        if(isinstance(int(requestid), int) == False):
            response = jsonify(
                {"requests": "You have entered an invalid request type"})
            response.status_code = 500
            return response

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
            requestUpdates = {
                "requestid": requestid,
                "requesttitle": request.json['requesttitle'],
                "requestdescription": request.json['requestdescription'],
                "requesttype": requesttype
            }
            dbmodel.updateRequest(requestUpdates)
            response = jsonify({"requests": "request edited"})
            response.status_code = 200
            return response


@app.route('/api/v2/users/logout', methods=['POST'])
def userLogout():

    if not defaultuserid['userid']:
        return jsonify({"Message": "You are not loged in"})
    defaultuserid['userid'] = 0
    response = jsonify({"response": "You have logged out"})
    response.status_code = 200
    return response


@app.route('/api/v2/requests', methods=['GET'])
@tokenRequired
def getAllRequest(currentUser):

    theRequests = dbmodel.getAllRequestForAdmin()
    if not theRequests:
        response = jsonify({"requests": "No requests yet"})
        response.status_code = 404
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response


#handlers


@app.errorhandler(404)
def pageNotFound(error):
    return jsonify({
        "Title": "Resource not found",
        "Message": "This resouce cannot be found"

    })


@app.errorhandler(405)
def notAllowed(error):
    return jsonify({
        "Title": "Not allowed",
        "Message": "You can not do this human. Check the mothod you are using"
    })


@app.errorhandler(500)
def fiveOo(error):
    return jsonify({
        "Title": "Server error",
        "Message": "Honestly, I din't see that coming."
    })
