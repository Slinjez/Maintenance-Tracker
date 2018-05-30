from flask import Flask, jsonify, request
import types
import pdb
#pdb.set_trace()

app = Flask(__name__)

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
        'requestcreationdate': '30 may 2018',
        'requeststatus': 1
    },
    {
        'requestid': 2,
        'requestorid': 2,
        'requesttitle': 'A Lame Title',
        'requestdescription': 'This is my request description',
        'requestcreationdate': '30 may 2018',
        'requeststatus': 1
    },
    {
        'requestid': 3,
        'requestorid': 2,
        'requesttitle': 'A Better Title',
        'requestdescription': 'This is my request description',
        'requestcreationdate': '30 may 2018',
        'requeststatus': 1
    }
]


@app.route('/')
def index():
    return "will be back with the ui soon"


@app.route('/api/v1/users/signup', methods=['POST'])
def signup():
    pass


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    pass

#all requests belonging to a user


@app.route('/api/v1/users/requests/<string:userid>', methods=['GET'])
def getAllRequests(userid):
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
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response

#all request with given id


@app.route('/api/v1/users/requestbyrequestid/<string:requestid>', methods=['GET'])
def getSingleRequest(requestid):
    if not requestid or requestid == None:
        requestid = 0
    try:
        if requestid is None or isinstance(int(requestid), int) == False:
            response = jsonify(
                {"requests": "You have entered an invalid reqest id"})
            response.status_code = 404
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
        response = jsonify({"requests": "No requests for this request id"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response

#just all requests no order


@app.route('/api/v1/users/requests', methods=['GET'])
def getAllUnfilteredRequest():

    theRequests = [request for request in requests]

    if not theRequests:
        response = jsonify({"requests": "No requests os for now"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response

#add request


@app.route('/api/v1/users/requests', methods=['POST'])
def createNewRequest():
    newrequest = {
        "requestid": request.json['requestid'],
        "requestorid": request.json['requestorid'],
        "requesttitle": request.json['requesttitle'],
        "requestdescription": request.json['requestdescription'],
        "requestcreationdate": request.json['requestcreationdate'],
        "requeststatus": request.json['requeststatus']
    }

    requests.append(newrequest)
    return jsonify({"allrequests": requests})


if __name__ == '__main__':
    app.run(debug=True)
