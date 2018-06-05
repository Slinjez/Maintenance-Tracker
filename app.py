from flask import Flask,jsonify, request
import pdb

app=Flask(__name__)

#some inits
users=[
    {
        'userid':1,
        'username':'daisy',
        'useremail':'daisy@daisy.com',
        'userpassword':'herps'
    },
    {
        'userid':2,
        'username':'thiga',
        'useremail':'mwangiwathiga@gmail.com',
        'userpassword':'myps'
    }
]

requests=[
    {
        'requestid':1,
        'requestorid':1,
        'requesttitle':'An Awesome Title',
        'requestdescription':'This is my request description',
        'requestcreationdate':'30 may 2018',
        'requeststatus':1
    },
    {
        'requestid':2,
        'requestorid':2,
        'requesttitle':'A Lame Title',
        'requestdescription':'This is my request description',
        'requestcreationdate':'30 may 2018',
        'requeststatus':1
    },
    {
        'requestid':3,
        'requestorid':2,
        'requesttitle':'A Better Title',
        'requestdescription':'This is my request description',
        'requestcreationdate':'30 may 2018',
        'requeststatus':1
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

@app.route('/maintenance_tracker/api/v1/getAllRequests/<int:userid>', methods=['GET'])
def getAllRequests(userid):
    userid=int(userid)
    
    theRequests=[request for request in requests if request['requestorid']==userid]
    #pdb.set_trace()

    response = jsonify({"requests":theRequests})
    response.status_code = 200
    return response


if __name__=='__main__':
    app.run(debug=True)