<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)
=======
#This file initializes in the application and brings together all of the various components.
import os
from flask import Flask
app = Flask(__name__)


# Import the application routes
from app import views
>>>>>>> ch-recreate-structure-158072403
