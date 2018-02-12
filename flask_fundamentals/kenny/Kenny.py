from flask import Flask, render_template, request, redirect, url_for, session
import os# Import Flask to allow us to create our app.

kenny = os.path.join('static', 'images')

app = Flask(__name__)
app.secret_key='ThisIsSecret'
app.config['flask_fundamentals'] = kenny

disappearing_ninjas = os.path.join('static', 'images')

@app.route('/')   
def index():      
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html', count = session['count'])                      

@app.route('/yes', methods=['GET'])
def gotoschool():
    return render_template('dead.html')

@app.route('/no', methods=['GET'])
def noschool():
    return render_template('noschool.html')

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

app.run(debug=True)     