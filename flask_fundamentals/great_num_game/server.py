from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key='ThisIsSecret'


@app.route('/')
def index ():

    if 'message' not in session:
        session ["message"] = ""
    if 'number' not in session:
        session['number'] = random.randint(1,101)
        print session['number']
    return render_template('index.html', message = session['message'])



@app.route('/usernum', methods=['POST'])
def userGuess():
    usernum = int(request.form['number'])
    if usernum > session['number']:
        session['message'] = "Too high!"
    elif usernum <  session['number']:
        session ['message'] = "Too Low!"
    else:
        session ['message'] = "You guessed the correct number!"
    return redirect('/')


@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')

app.run(debug=True)



