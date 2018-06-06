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
defaultuserid = 2
users = [
    
]

requests = [
    
]


@app.route('/')
def index():
    return "will be back with the ui soon"


@app.route('/api/v1/users/signup', methods=['POST'])
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

    elif len(userps1)<=3:
        response = jsonify({"response": "Enter a password more than 4 charachters"})
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
        #pdb.set_trace()
        #hashedpassword=generate_password_hash(userps1, method='sha256')
        hashedpassword=generate_password_hash(userps1, method='sha256')
        newsignuprequest = {
            #"userid": lastid,
            "userid": str(uuid.uuid4()),
            "username": request.json["username"],
            "useremail": request.json["useremail"],
            "userpassword": hashedpassword
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

@app.route('/api/v1/users/getusers/', methods=['GET'])
def getAllUsers():
    response=jsonify({"users":users})
    return response

@app.route('/api/v1/users/login1', methods=['POST'])
def login1():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response("1could not verify", 401,{'WWW-Authenticate':'Basic realm="Login Required"'})
    
    user= [theuser for theuser in users if theuser["username"] == auth.username]
    print(users)

    if not user:
        return make_response("2could not verify", 401,{'WWW-Authenticate':'Basic realm="Login Required"'})

    if check_password_hash(user['userpassword'],auth.password):
        token=jwt.encode({'publicid':user['userid'], 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({"token":token.decode('UTF-8')})

    return make_response("3could not verify", 401,{'WWW-Authenticate':'Basic realm="Login Required"'})


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    usermail = request.json["useremail"]
    userps = request.json["userpassword"]
    hashedpassword=generate_password_hash(userps, method='sha256')
    #pdb.set_trace()
    if not usermail:
        response = jsonify({"response": "email is required"})
        response.status_code = 400
        return response

    elif len(userps)<=3:
        response = jsonify({"response": "Enter a password more than 4 charachters"})
        response.status_code = 400
        return response

    elif not userps:
        response = jsonify({"response": "password is required"})
        response.status_code = 400
        return response
    else:
        theRequests = [
            theuser for theuser in users if theuser["useremail"] == usermail]
        if not theRequests:
            response = jsonify({"response": "Unregistered email"})
            response.status_code = 400
            return response
        else:            
            correctps = theRequests[0]['userpassword']
            #pdb.set_trace()
            if check_password_hash(correctps,userps) != True:
                print("ps mismatch")
                response = jsonify({"response": "Invalid credentials"})
                response.status_code = 400
                return response
            else:
                token=jwt.encode({'publicid':theRequests[0]['userid'], 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

                return jsonify({"token":token.decode('UTF-8')})
                
                # response = jsonify({"response": "logged in correctly"})
                # response.status_code = 200
                # return response


#all requests belonging to a user defaultuserid
@app.route('/api/v1/users/requests', methods=['GET'])
def getAllRequests():
    
    if not request.json["userid"]:
        userid=defaultuserid
        #pdb.set_trace()
    else:
        userid=request.json["userid"]
    
    theRequests = [
        request for request in requests if request["requestorid"] == userid]

    if not theRequests:
        response = jsonify({"requests": "No requests for this user"})
        response.status_code = 404
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response

#one request for a given user (enter from url)


@app.route('/api/v1/users/requests/<string:requestid>', methods=['GET'])
def getSingleRequest(requestid):
    
    
    if not requestid or requestid == None:
        #requestid = request.json["requestid"]
        response = jsonify({"response": "You have not entered an invalid request id"})
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
    
    theRequests = [
        request for request in requests if request["requestid"] == requestid]
    
    if not theRequests:
        response = jsonify({"requests": "This request does not exist"})
        response.status_code = 404        
        return response
        pdb.set_trace()
    else:
        
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response


#add request
@app.route('/api/v1/users/requests', methods=['POST'])
def createNewRequest():
    #defUsr=defaultuserid
    #pdb.set_trace()
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
        response=jsonify({"response": "Enter request title"})
        response.status_code = 206
        return response
    elif not requestdescription:
        response=jsonify({"response": "Enter request description"})
        response.status_code = 206
        return response
    elif not requesttype:
        response=jsonify({"response": "Enter request type"})
        response.status_code = 206
        return response
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
        response=jsonify({"response": "Created '"+requesttitle+"' request successfully"})
        response.status_code = 200
        return response

#and finally edit a request
@app.route('/api/v1/users/requests/<string:requestid>', methods=['PUT'])
def updateRequest(requestid):
    #pdb.set_trace()
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
        response = jsonify({"respons": "Cannot edit this request because its missing"})
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
