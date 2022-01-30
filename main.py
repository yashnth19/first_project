
from flask import Flask

from wsgiref import simple_server

from flask import Flask, render_template, request
from training_data_validation import training_data_validator
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
#flask is a web application framework written in python

import atexit
import uuid
import os
app = Flask(__name__) #creates a WSGI application
dashboard.bind(app)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/folder_path_getter', methods=['GET', 'POST'])
@cross_origin()
def trainer():
    if request.method=='POST' :
        folder=request.form['path']
        tran_obj=training_data_validator()
        tran_obj.check_logger()
    return "Folder destination is " + folder

@app.route('/predictor', methods=['GET', 'POST'])
@cross_origin()
def trainer2():
    if request.method=='POST' :
        folder=request.form['path1']

    return "Folder destination is " + folder
port = int(os.getenv("PORT", 5000))

if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()