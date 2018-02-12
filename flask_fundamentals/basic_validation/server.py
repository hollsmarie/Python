
from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    # if 'message' not in session:
    #     session ['message'] = ""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        #session ['message'] = "Enter a valid name"
        flash ("Please enter a valid name")
    else:
        #session ['message'] = "success!"
        flash ("Success! Your name is {}".format(request.form['name']))
    return redirect('/')
app.run(debug=True)




