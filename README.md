# Maintenance-Tracker [![Build Status](https://travis-ci.org/Slinjez/Maintenance-Tracker.svg?branch=ch-cleanup-code-158239458)](https://travis-ci.org/Slinjez/Maintenance-Tracker)[![Maintainability](https://api.codeclimate.com/v1/badges/89328b248d2e49fea8e5/maintainability)](https://codeclimate.com/github/Slinjez/Maintenance-Tracker/maintainability)[![Coverage Status](https://coveralls.io/repos/github/Slinjez/Maintenance-Tracker/badge.svg?branch=develop)](https://coveralls.io/github/Slinjez/Maintenance-Tracker?branch=develop)
This is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

Here are some of its features:
  - Users can create an account and log in.
  - The users should be able to make maintenance or repairs request.
  - An admin should be able to approve/reject a repair/maintenance request.
  - The admin should be able to mark request as resolved once it is done.
  - The admin should be able to view all maintenance/repairs requests on the application
  - The admin should be able to filter requests
  - The user can view all his/her requests
  
Build using:
  * [Python] Flask microframework
  * [HTML5 CSS3] Layout and styling
  * [JavaScript] Enhancing UI functionality
  * [Postgres] For data storage

### Installation
Maintenance-Tracker requires Python 3.6 installed inorder to run
Cclone this repository on your computer
Navigate to folder containing project on terminal
```sh
$ pip install virtualenv
$ virtualenv venv
$ pip install -r requirements.txt
$ python run.py
```
### Current Endpoints 
| Endpoint | Description |
| ------ | ------ |
| POST /auth/signup | Register a user |
| POST /auth/login | Login a user |
| GET /users/requests  | Fetch all the requests of a logged in user |
| GET /users/requests/<requestId> | Fetch a request that belongs to a logged in user |
| POST /users/requests | Create a request. |
| PUT /users/requests/<requestId> | Modify a request. |
| Get /requests/  | Fetch all the requests. |
| PUT /requests/<requestId>/approve | Approve request |
| PUT /requests/<requestId>/disapprove | Disapprove request |
| PUT /requests/<requestId>/resolve | Resolve request |
| PUT /requests/logout | Logout from system |

### Proposed UI
https://slinjez.github.io/Maintenance-Tracker/UI/

![alt text](https://ibb.co/gQRL3T)
https://ibb.co/gQRL3T

https://ibb.co/iLPUxo

https://ibb.co/kAyYOT


