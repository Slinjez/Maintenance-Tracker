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


@app.route('/maintenance_tracker/api/v1/signup', methods=['POST'])
def signup():
    pass


@app.route('/maintenance_tracker/api/v1/login', methods=['POST'])
def login():
    pass


@app.route('/maintenance_tracker/api/v1/getAllRequests/<string:userid>', methods=['GET'])
def getAllRequests(userid):
    if not userid or userid==None:
        userid=0
    try:
        if userid is None or isinstance(int(userid),int)==False:
            response = jsonify({"requests": "You have entered an invalid user id"})
            response.status_code = 200
            return response
        else:
            userid = int(userid)
    except:
        response = jsonify({"requests": "You have entered an invalid user id"})
        response.status_code = 405 #Method not allowed
        return response

    theRequests = [request for request in requests if request["requestorid"] == userid]

    if not theRequests:
        response = jsonify({"requests": "No requests for this user"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response

@app.route('/maintenance_tracker/api/v1/getSingleRequest/<string:requestid>', methods=['GET'])
def getSingleRequest(requestid):
    if not requestid or requestid==None:
        requestid=0
    try:
        if requestid is None or isinstance(int(requestid),int)==False:
            response = jsonify({"requests": "You have entered an invalid reqest id"})
            response.status_code = 404
            return response
        else:
            requestid = int(requestid)
    except:
        response = jsonify({"requests": "You have entered an invalid request id"})
        response.status_code = 405 #Method not allowed
        return response

    theRequests = [request for request in requests if request["requestid"] == requestid]

    if not theRequests:
        response = jsonify({"requests": "No requests for this request id"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"requests": theRequests})
        response.status_code = 200
        return response


if __name__ == '__main__':
    app.run(debug=True)
