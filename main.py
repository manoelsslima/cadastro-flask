from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = MySQL(app) # setting configurations

from views import *

# ensure that run() method will be executed only by Python e not by any other file
if __name__ == '__main__':
    app.run(debug=True)