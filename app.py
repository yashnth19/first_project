from flask import Flask, render_template, request
from training_data_validation import training_data_validator
app = Flask(__name__)  #creates a WSGI application


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/folder_path_getter', methods=['GET', 'POST'])
def trainer():
    if request.method=='POST' :
        folder=request.form['path']
        tran_obj=training_data_validator()
        tran_obj.check_logger()
    return "Folder destination is " + folder

@app.route('/predictor', methods=['GET', 'POST'])
def trainer2():
    if request.method=='POST' :
        folder=request.form['path1']

    return "Folder destination is " + folder

if __name__ == "__main__":
    # app.run(host="0.0.0.0",port=5000)
    app.run()